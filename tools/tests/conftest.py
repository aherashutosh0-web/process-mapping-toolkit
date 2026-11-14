import sys
from pathlib import Path

# Make tools/ importable so tests can `import validate_rtm` regardless of cwd.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
