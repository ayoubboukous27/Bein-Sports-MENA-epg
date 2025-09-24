import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator

epg_url = "https://iptvx.one/EPG"
output_file = "epg_iptvx_ar.xml"

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

print("⏳ جاري تحميل ملف EPG ...")
response = requests.get(epg_url)
response.raise_for_status()

with open("epg_iptvx.xml", "wb") as f:
    f.write(response.content)

print("✅ تم التحميل، جاري الترجمة ...")
tree = ET.parse("epg_iptvx.xml")
root = tree.getroot()

for programme in root.findall("programme"):
    for tag in ["title", "desc", "category"]:
        for elem in programme.findall(tag):
            if elem.text:
                elem.text = translate_text(elem.text)
                elem.set("lang", "ar")

tree.write(output_file, encoding="utf-8", xml_declaration=True)
print(f"✅ تم إنشاء الملف المترجم: {output_file}")
