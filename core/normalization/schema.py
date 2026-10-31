from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class UnifiedPage:
    url: str
    title: str | None = None
    meta_description: str | None = None
    canonical_url: str | None = None
    h1_headers: List[str] = field(default_factory=list)
    word_count: int = 0
    load_time_seconds: float = 0.0
    has_schema_org: bool = False
    broken_links: List[str] = field(default_factory=list)


@dataclass
class UnifiedPost:
    platform: str
    post_id: str
    url: str
    title: str
    views: int = 0
    likes: int = 0
    comments: int = 0
    shares: int = 0
    engagement_rate: float = 0.0
    hashtags: List[str] = field(default_factory=list)


@dataclass
class UnifiedDataset:
    project_id: str
    domain: str
    normalized_at: str
    pages: List[UnifiedPage] = field(default_factory=list)
    posts: List[UnifiedPost] = field(default_factory=list)
    metrics_summary: Dict[str, Any] = field(default_factory=dict)
