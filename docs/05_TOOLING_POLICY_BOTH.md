# تنظیم ابزارهای دوره پایتون — روش BOTH

## تصمیم آموزشی ثبت‌شده
روش انتخابی هنرجو: **BOTH**؛ یعنی یادگیری عملی هر دو روش استاندارد Python و ابزار مدرن `uv`.

## ابزارهای اصلی
1. Python 3.14.x پایدار
2. Visual Studio Code
3. افزونه Python از Microsoft در VS Code
4. PowerShell (یا ترمینال داخلی VS Code)
5. `pip` و `venv`؛ ابزارهای استاندارد همراه Python
6. `uv`؛ ابزار مکمل برای مدیریت نسخه Python، محیط مجازی، وابستگی‌ها و اجرای پروژه

## سیاست استفاده در دوره
- هنرجو ابتدا مفهوم محیط مجازی و نصب بسته را با `venv` و `pip` می‌آموزد.
- همان کارها را با `uv` نیز انجام می‌دهد تا تفاوت فرمان‌ها و گردش کار را بشناسد.
- در پروژه‌های کوچک آموزشی، هر دو روش قابل استفاده‌اند.
- در پروژه‌های جدی‌تر، `uv` گزینه پیشنهادی برای مدیریت سریع‌تر و یکپارچه پروژه است؛ اما دانستن `pip` و `venv` همچنان ضروری است.
- نصب کتابخانه غیرضروری در جلسات ابتدایی انجام نمی‌شود.
- `Git` در مرحله مهارت حرفه‌ای پایه نصب و آموزش داده می‌شود؛ فعلاً اجباری نیست.
- `Jupyter` و کتابخانه‌های جانبی تا زمان نیاز نصب نمی‌شوند.

## فرمان‌های مرجع

### بررسی Python و pip
در PowerShell:
```powershell
py --version
python --version
py -m pip --version
```

### روش استاندارد: venv و pip
```powershell
mkdir demo-pip
cd demo-pip
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install requests
python -m pip freeze
deactivate
```

اگر فعال‌سازی به دلیل Execution Policy مسدود شد، فعلاً می‌توان بدون فعال‌سازی از مفسر محیط مجازی استفاده کرد:
```powershell
.venv\Scripts\python.exe -m pip install requests
.venv\Scripts\python.exe -m pip freeze
```

### روش uv
```powershell
uv --version
uv init demo-uv
cd demo-uv
uv add requests
uv run python -c "import requests; print(requests.__version__)"
```

## نصب uv در Windows
در PowerShell:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
پس از نصب، PowerShell را ببندید و دوباره باز کنید:
```powershell
uv --version
```

## بررسی VS Code
در VS Code > Extensions بررسی شود که افزونه **Python** با ناشر **Microsoft** نصب باشد. در صورت پیشنهاد، **Pylance** و **Python Debugger** نیز نصب شوند.

## پوشه تمرین پیشنهادی
```text
Documents/
└── Python-Learning/
    ├── lessons/
    ├── exercises/
    └── projects/
```

## وضعیت فعلی آماده‌سازی
- سیستم‌عامل: Windows 11 (طبق اعلام هنرجو)
- Python: نصب است؛ نسخه و اجرای صحیح هنوز با فرمان‌ها تأیید نشده
- VS Code: نصب است؛ افزونه Python هنوز تأیید نشده
- pip: باید با `py -m pip --version` بررسی شود
- venv: همراه Python در دسترس است؛ هنوز ساخت و اجرای آزمایشی تأیید نشده
- uv: نصب آن هنوز تأیید نشده
- اجرای اولین فایل `hello.py`: هنوز تأیید نشده
- جلسات آموزشی تکمیل‌شده: 0 از 24
- مرحله: آماده‌سازی پیش از جلسه 1
- درصد ساختاری دوره: 0٪

## شرط عبور از آماده‌سازی
وقتی نسخه Python و pip تأیید شد، افزونه Python در VS Code نصب بود، `uv --version` موفق اجرا شد، و فایل `hello.py` با `py hello.py` خروجی درست داد، آماده شروع جلسه 1 هستیم.
