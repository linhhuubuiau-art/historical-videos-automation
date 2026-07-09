import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_json(relative_path: str) -> dict:
    return json.loads((PROJECT_ROOT / relative_path).read_text(encoding="utf-8"))


def scene_output_dir(project_name: str, kind: str) -> Path:
    path = PROJECT_ROOT / "generated" / kind / project_name
    path.mkdir(parents=True, exist_ok=True)
    return path
