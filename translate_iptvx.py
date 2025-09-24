import requests
import xml.etree.ElementTree as ET
import gzip
import io
from deep_translator import GoogleTranslator

epg_url = "https://iptvx.one/EPG7"
output_file = "epg_source_ar.xml"

translator = GoogleTranslator(source="auto", target="ar")
cache = {}

def translate_text(text):
    if not text:
        return ""
    if text in cache:
        return cache[text]
    try:
        translated = translator.translate(text)
        cache[text] = translated
        return translated
    except Exception:
        return text

print(f"⏳ جاري تحميل ملف EPG من {epg_url} ...")
response = requests.get(epg_url, headers={"User-Agent": "Mozilla/5.0"})
response.raise_for_status()

content = response.content

# فك ضغط gzip إذا لزم
if response.headers.get("Content-Encoding") == "gzip" or epg_url.endswith(".gz"):
    content = gzip.decompress(content)

# حفظ نسخة خام
with open("epg_source_raw.txt", "wb") as f:
    f.write(content)

# نعاين البداية
preview = content[:500].decode("utf-8", errors="ignore")
print("📄 معاينة أول 500 بايت:\n", preview)

# نتأكد إذا الملف فعلاً XML
if not preview.strip().startswith("<?xml") and "<tv" not in preview:
    raise ValueError("🚨 الملف المحمّل ليس XML صالح (يبدو أنه HTML أو رسالة خطأ من السيرفر).")

print("✅ الملف يبدو XML صالح، جاري الترجمة ...")
tree = ET.parse(io.BytesIO(content))
root = tree.getroot()

for programme in root.findall("programme"):
    for tag in ["title", "desc", "category"]:
        for elem in programme.findall(tag):
            if elem.text:
                elem.text = translate_text(elem.text)
                elem.set("lang", "ar")

tree.write(output_file, encoding="utf-8", xml_declaration=True)
print(f"✅ تم إنشاء الملف المترجم: {output_file}")
