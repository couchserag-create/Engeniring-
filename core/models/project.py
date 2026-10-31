from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class StageState:
    id: str
    label: str
    status: str = "not_started"
    updated_at: str | None = None
    note: str | None = None


@dataclass
class Project:
    project_id: str
    name: str
    project_type: str
    pipeline_label: str | None = None
    domain: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    stages: Dict[str, StageState] = field(default_factory=dict)
    history: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "project_id": self.project_id,
            "name": self.name,
            "type": self.project_type,
            "domain": self.domain,
            "pipeline_label": self.pipeline_label,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "stages": {k: {"label": v.label, "status": v.status, "updated_at": v.updated_at, "note": v.note} for k, v in self.stages.items()},
            "history": self.history,
        }
