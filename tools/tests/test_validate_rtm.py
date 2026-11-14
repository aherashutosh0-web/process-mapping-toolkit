"""Tests for validate_rtm.py. Run from the repo root with: python -m pytest"""

from pathlib import Path

import pytest

from validate_rtm import RTMError, coverage_stats, load_rtm, main, validate_rtm

TOOLS_DIR = Path(__file__).resolve().parents[1]
SAMPLE_CSV = TOOLS_DIR / "sample_data" / "rtm_sample.csv"

HEADER = "ReqID,Requirement,Source,Owner,Priority,TestCaseIDs,Status\n"


def write_csv(tmp_path, body: str) -> Path:
    path = tmp_path / "rtm.csv"
    path.write_text(HEADER + body, encoding="utf-8")
    return path


# --- the sample file -------------------------------------------------------

def test_sample_data_finds_the_seeded_problems():
    rows = load_rtm(SAMPLE_CSV)
    findings = validate_rtm(rows)
    codes = {f.code for f in findings}

    assert "MISSING_COVERAGE" in codes      # BA-005 has a source but no tests
    assert "ORPHANED_REQ" in codes          # BA-011 has neither source nor tests
    assert "MISSING_FIELD" in codes         # BA-011 has an empty Requirement
    assert "MALFORMED_TEST_ID" in codes     # BA-013 references 'TC-17A'

    uncovered = {f.req_id for f in findings if f.code == "MISSING_COVERAGE"}
    assert uncovered == {"BA-005"}


def test_sample_data_coverage_stats():
    rows = load_rtm(SAMPLE_CSV)
    stats = coverage_stats(rows)
    assert stats["requirements"] == 14
    assert stats["uncovered"] == 2          # BA-005, BA-011
    assert stats["coverage_pct"] == pytest.approx(85.7, abs=0.1)


# --- clean input -----------------------------------------------------------

def test_clean_csv_has_no_findings(tmp_path):
    path = write_csv(
        tmp_path,
        "BA-001,Orders must validate stock.,Workshop,A. Patel,must,TC-001,Approved\n"
        "BA-002,Cancel allowed pre-dispatch.,Interview,A. Patel,should,TC-002;TC-003,Approved\n",
    )
    assert validate_rtm(load_rtm(path)) == []


# --- individual checks -----------------------------------------------------

def test_duplicate_reqid_detected(tmp_path):
    path = write_csv(
        tmp_path,
        "BA-001,First.,Workshop,A. Patel,must,TC-001,Approved\n"
        "BA-001,Duplicate id.,Workshop,A. Patel,must,TC-002,Approved\n",
    )
    findings = validate_rtm(load_rtm(path))
    assert any(f.code == "DUPLICATE_REQ_ID" and f.req_id == "BA-001" for f in findings)


def test_missing_coverage_vs_orphaned(tmp_path):
    path = write_csv(
        tmp_path,
        "BA-001,Has source but no tests.,Workshop,A. Patel,must,,Approved\n"
        "BA-002,No source and no tests.,,A. Patel,must,,Draft\n",
    )
    findings = validate_rtm(load_rtm(path))
    assert any(f.code == "MISSING_COVERAGE" and f.req_id == "BA-001" for f in findings)
    assert any(f.code == "ORPHANED_REQ" and f.req_id == "BA-002" for f in findings)


def test_malformed_test_id_detected(tmp_path):
    path = write_csv(tmp_path, "BA-001,Needs tests.,Workshop,A. Patel,must,TC-1;Test Case 2,Approved\n")
    findings = validate_rtm(load_rtm(path))
    malformed = [f for f in findings if f.code == "MALFORMED_TEST_ID"]
    assert len(malformed) == 2


def test_bad_priority_detected(tmp_path):
    path = write_csv(tmp_path, "BA-001,Odd priority.,Workshop,A. Patel,urgent,TC-001,Approved\n")
    findings = validate_rtm(load_rtm(path))
    assert any(f.code == "BAD_PRIORITY" and f.req_id == "BA-001" for f in findings)


def test_custom_pattern_is_respected(tmp_path):
    path = write_csv(tmp_path, "BA-001,Custom scheme.,Workshop,A. Patel,must,TC_001,Approved\n")
    rows = load_rtm(path)
    assert any(f.code == "MALFORMED_TEST_ID" for f in validate_rtm(rows))
    assert validate_rtm(rows, test_id_pattern=r"TC_\d{3}") == []


# --- error handling & CLI --------------------------------------------------

def test_missing_column_raises(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("ReqID,Requirement\nBA-001,Hello\n", encoding="utf-8")
    with pytest.raises(RTMError, match="missing required column"):
        load_rtm(path)


def test_missing_file_raises(tmp_path):
    with pytest.raises(RTMError, match="file not found"):
        load_rtm(tmp_path / "nope.csv")


def test_main_exit_codes(tmp_path, capsys):
    clean = write_csv(tmp_path, "BA-001,Fine.,Workshop,A. Patel,must,TC-001,Approved\n")
    assert main([str(clean)]) == 0
    assert "0 finding(s)" in capsys.readouterr().out

    dirty = write_csv(tmp_path, "BA-001,Untested.,Workshop,A. Patel,must,,Approved\n")
    assert main([str(dirty)]) == 1

    assert main([str(tmp_path / "missing.csv")]) == 2
