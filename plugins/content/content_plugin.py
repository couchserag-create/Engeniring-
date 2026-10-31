from __future__ import annotations
from typing import Any, Dict

from plugins.base import BasePlugin


class ContentPlugin(BasePlugin):
    @property
    def name(self) -> str:
        return "content"

    @property
    def label(self) -> str:
        return "Content Quality Engine"

    def analyze(self, dataset: Any) -> Dict[str, Any]:
        pages = dataset.pages
        recommendations = []
        thin_pages = [p.url for p in pages if p.word_count < 300]
        score = 84

        if thin_pages:
            score -= len(thin_pages) * 6
            recommendations.append({
                "title": "إضافة محتوى أكثر عمقًا على الصفحات ذات النص الضعيف",
                "priority": "HIGH",
                "impact": 7,
                "effort": 3,
                "evidence": thin_pages[:5],
                "benchmark": "الصفحات الرائدة تحتوي غالبًا على أكثر من 800 كلمة"
            })

        return {
            "plugin_name": self.name,
            "label": self.label,
            "score": max(0, score),
            "recommendations": recommendations,
            "evidence_summary": {
                "pages_analyzed": len(pages),
                "thin_pages": len(thin_pages),
            },
        }
