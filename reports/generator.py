from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict


def render_html_report(project_id: str, domain: str, plugin_results: Dict[str, Any], summary: str) -> str:
    cards = []
    for name, result in plugin_results.items():
        rec_html = "".join(
            f"""
            <div class="rec">
              <strong>{rec.get('title', '')}</strong>
              <div class="meta">الأولوية: {rec.get('priority', '')} | الدليل: {', '.join(str(x) for x in rec.get('evidence', []))}</div>
            </div>
            """
            for rec in result.get("recommendations", [])
        )
        cards.append(f"""
        <div class="card">
          <h2>{result.get('label', name)}</h2>
          <div class="score">{result.get('score', 0)} / 100</div>
          {rec_html}
        </div>
        """)

    return f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <title>تقرير TeamWork — {domain}</title>
  <style>
    body {{ font-family: Tahoma, Arial, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 40px; }}
    .container {{ max-width: 1000px; margin: 0 auto; background: #111827; border: 1px solid #374151; border-radius: 16px; padding: 28px; }}
    h1 {{ color: #7dd3fc; margin-bottom: 12px; }}
    .card {{ background: #1f2937; border: 1px solid #374151; border-radius: 12px; padding: 18px; margin-top: 20px; }}
    .score {{ font-size: 28px; font-weight: bold; color: #34d399; }}
    .rec {{ border-right: 4px solid #fbbf24; padding-right: 12px; margin-top: 10px; }}
    .meta {{ color: #9ca3af; font-size: 12px; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>تقرير التحليل الشامل — {domain}</h1>
    <div class="score">ملخص تنفيذي: {summary}</div>
    {''.join(cards)}
  </div>
</body>
</html>
"""


def save_report_files(project_id: str, output_dir: Path, domain: str, plugin_results: Dict[str, Any], summary: str):
    output_dir.mkdir(parents=True, exist_ok=True)
    html_path = output_dir / "executive_report.html"
    json_path = output_dir / "final_report.json"

    with html_path.open("w", encoding="utf-8") as f:
        f.write(render_html_report(project_id, domain, plugin_results, summary))

    payload = {
        "project_id": project_id,
        "domain": domain,
        "summary": summary,
        "plugin_results": plugin_results,
    }
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    return html_path, json_path
