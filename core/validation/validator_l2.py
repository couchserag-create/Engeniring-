from __future__ import annotations
from typing import Any, Dict, List, Tuple


def validate_analysis_consistency(plugin_results: Dict[str, Any]) -> Tuple[bool, str, List[str]]:
    issues: List[str] = []
    total_recommendations = 0
    missing_evidence = 0

    for plugin_name, result in plugin_results.items():
        recommendations = result.get("recommendations", [])
        for rec in recommendations:
            total_recommendations += 1
            if not rec.get("evidence"):
                missing_evidence += 1
                issues.append(f"التوصية '{rec.get('title', '')}' في {plugin_name} تفتقر إلى أدلة.")

    confidence = "high"
    if missing_evidence > 0:
        confidence = "medium"
    if missing_evidence > max(total_recommendations // 2, 1) and total_recommendations > 0:
        confidence = "low"

    if not plugin_results:
        issues.append("لا توجد نتائج من المحركات.")
        confidence = "none"

    is_valid = (confidence in ["high", "medium"]) and bool(plugin_results)
    return is_valid, confidence, issues
