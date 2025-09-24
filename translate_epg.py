import requests
import xml.etree.ElementTree as ET
import io
from deep_translator import MyMemoryTranslator

# ملف Bein EPG كمصدر
input_file = "epg_mapped_with_logos.xml"
output_file = "epg_mapped_with_logos_ar.xml"

translator = MyMemoryTranslator(source="en", target="ar")
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
        return text  # fallback لو فشل

print("⏳ جاري قراءة ملف EPG ...")
tree = ET.parse(input_file)
root = tree.getroot()

print("✅ جاري الترجمة باستخدام MyMemory ...")
for programme in root.findall("programme"):
    for tag in ["title", "desc", "category"]:
        for elem in programme.findall(tag):
            if elem.text:
                elem.text = translate_text(elem.text)
                elem.set("lang", "ar")

tree.write(output_file, encoding="utf-8", xml_declaration=True)
print(f"✅ تم إنشاء الملف المترجم: {output_file}")
