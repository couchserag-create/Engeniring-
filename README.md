# TeamWork

نظام إدارة المشاريع والتحليل الاستشاري، مبني على فكرة "Project Operating System":
- لكل مشروع lifecycle مستقل
- لكل مرحلة حالة واضحة (not_started / in_progress / completed / partial / blocked)
- كل مرحلة تنتج output
- كل تحليل يعتمد على Evidence
- كل تقرير نهائي يقرأ مخرجات المحطات فقط

## المزايا
- إدارة المشاريع عبر CLI
- سجل كامل للتاريخ والحالة
- تنقية/تطبيع البيانات قبل التحليل
- محركات تحليل مستقلة (plugins)
- تقرير HTML نهائي
- لوحة تحكم ويب للاستعراض

## التشغيل السريع

### 1) تثبيت البيئة
```bash
python -m venv .venv
source .venv/bin/activate
# أو في Windows:
# .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) إنشاء مشروع
```bash
python pipeline.py init --project-id arab-audit-001 --name "Arab Computer" --type company_intelligence --domain arabcomputer.net
python pipeline.py init --project-id egypt-history-001 --name "حلقة تاريخ مصر" --type content_marketing
```

### 3) تحديث حالة مرحلة
```bash
python pipeline.py advance --project-id egypt-history-001 --stage research_evidence --status in_progress --note "بدأ جمع المصادر"
```

### 4) تشغيل pipeline
```bash
python pipeline.py run --project-id arab-audit-001
```

### 5) عرض الحالة
```bash
python pipeline.py status --project-id arab-audit-001
```

### 6) تشغيل اللوحة
```bash
python server.py
```

ثم افتح:
http://localhost:8787

## هيكل المشروع
- `pipeline.py`: CLI manager
- `server.py`: dashboard API
- `config/pipelines.json`: تعريف المسارات
- `core/`: النماذج، التخزين، التحقق، التطبيع
- `plugins/`: محركات التحليل المستقلة
- `reports/`: توليد HTML وJSON
- `runs/<project-id>/`: ملفات المشروع والمخرجات
- `dashboard/`: الصفحة الرئيسية
