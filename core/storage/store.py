from __future__ import annotations

import json
from pathlib import Path


class JSONStore:
    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def save_json(self, path: str | Path, data: dict) -> None:
        target = Path(path) if isinstance(path, Path) else self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")

    def load_json(self, path: str | Path) -> dict:
        target = Path(path) if isinstance(path, Path) else self.root / path
        with target.open("r", encoding="utf-8") as f:
            return json.load(f)
