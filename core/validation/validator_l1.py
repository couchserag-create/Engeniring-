from __future__ import annotations
from typing import Any, Dict, List, Tuple


def validate_raw_data_sufficiency(raw_data: Dict[str, Any], min_pages: int = 1, min_posts: int = 0) -> Tuple[bool, List[str]]:
    gaps: List[str] = []

    pages = raw_data.get("pages", [])
    if len(pages) < min_pages:
        gaps.append(f"عدد الصفحات المجمعة ({len(pages)}) أقل من الحد الأدنى ({min_pages}).")

    total_posts = len(raw_data.get("youtube", [])) + len(raw_data.get("facebook", [])) + len(raw_data.get("tiktok", []))
    if total_posts < min_posts:
        gaps.append(f"إجمالي منشورات السوشيال المجمعة ({total_posts}) أقل من الحد الأدنى ({min_posts}).")

    if not raw_data.get("domain"):
        gaps.append("النطاق (domain) غير محدد.")

    return (len(gaps) == 0), gaps
