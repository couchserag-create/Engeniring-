from __future__ import annotations
from typing import Any, Dict

from plugins.base import BasePlugin


class SEOPlugin(BasePlugin):
    @property
    def name(self) -> str:
        return "seo"

    @property
    def label(self) -> str:
        return "SEO Engine"

    def analyze(self, dataset: Any) -> Dict[str, Any]:
        pages = dataset.pages
        recommendations = []
        low_quality_pages = [p.url for p in pages if not p.title or p.word_count < 200]
        score = 90

        if low_quality_pages:
            score -= len(low_quality_pages) * 7
            recommendations.append({
                "title": "إثراء عناوين الصفحات ومحتواها لتقوية الظهور في البحث",
                "priority": "HIGH",
                "impact": 8,
                "effort": 2,
                "evidence": low_quality_pages[:5],
                "benchmark": "أفضل المواقع تحقق أرقامًا أعلى من 80% في جودة المحتوى"
            })

        return {
            "plugin_name": self.name,
            "label": self.label,
            "score": max(0, score),
            "recommendations": recommendations,
            "evidence_summary": {
                "pages_analyzed": len(pages),
                "pages_with_issues": len(low_quality_pages),
            },
        }
