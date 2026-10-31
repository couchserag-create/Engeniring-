from __future__ import annotations
from typing import Any, Dict, List

from core.normalization.schema import UnifiedDataset, UnifiedPage, UnifiedPost


def transform_web_pages(raw_pages: List[Dict[str, Any]]) -> List[UnifiedPage]:
    pages: List[UnifiedPage] = []
    for page in raw_pages:
        pages.append(
            UnifiedPage(
                url=page.get("url", ""),
                title=page.get("title"),
                meta_description=page.get("meta_description"),
                canonical_url=page.get("canonical_url"),
                h1_headers=page.get("h1_headers", []),
                word_count=int(page.get("word_count", 0)),
                load_time_seconds=float(page.get("load_time_seconds", 0.0)),
                has_schema_org=bool(page.get("has_schema_org", False)),
                broken_links=page.get("broken_links", []),
            )
        )
    return pages


def transform_posts(raw_posts: List[Dict[str, Any]], platform: str) -> List[UnifiedPost]:
    posts: List[UnifiedPost] = []
    for item in raw_posts:
        posts.append(
            UnifiedPost(
                platform=platform,
                post_id=str(item.get("id", item.get("post_id", ""))),
                url=item.get("url", ""),
                title=item.get("title", item.get("text", ""))[:120],
                views=int(item.get("views", item.get("view_count", 0))),
                likes=int(item.get("likes", item.get("reactions", 0))),
                comments=int(item.get("comments", item.get("comment_count", 0))),
                shares=int(item.get("shares", item.get("share_count", 0))),
                engagement_rate=float(item.get("engagement_rate", 0.0)),
                hashtags=item.get("hashtags", []),
            )
        )
    return posts


def normalize_all_data(project_id: str, domain: str, raw_data: Dict[str, Any]) -> UnifiedDataset:
    pages = transform_web_pages(raw_data.get("pages", []))
    posts: List[UnifiedPost] = []
    for platform, entries in [("youtube", raw_data.get("youtube", [])), ("facebook", raw_data.get("facebook", [])), ("tiktok", raw_data.get("tiktok", []))]:
        posts.extend(transform_posts(entries, platform))

    total_engagement = sum(p.engagement_rate for p in posts)
    avg_engagement = round(total_engagement / max(len(posts), 1), 4)

    metrics_summary = {
        "total_posts": len(posts),
        "total_pages": len(pages),
        "average_engagement_rate": avg_engagement,
        "platforms_detected": sorted({p.platform for p in posts}),
    }

    return UnifiedDataset(
        project_id=project_id,
        domain=domain,
        normalized_at="2026-01-01T00:00:00Z",
        pages=pages,
        posts=posts,
        metrics_summary=metrics_summary,
    )
