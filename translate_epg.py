import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator

input_file = "epg_mapped_with_logos.xml"
output_file = "epg_mapped_with_logos_ar.xml"

translator = GoogleTranslator(source="auto", target="ar")
cache = {}  # لتجنب إعادة الترجمة لنفس النصوص

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

print("⏳ جاري الترجمة ...")

tree = ET.parse(input_file)
root = tree.getroot()

for programme in root.findall("programme"):
    # نترجم العنوان
    for elem in programme.findall("title"):
        if elem.text:
            elem.text = translate_text(elem.text)
            elem.set("lang", "ar")

    # نترجم الوصف
    for elem in programme.findall("desc"):
        if elem.text:
            elem.text = translate_text(elem.text)
            elem.set("lang", "ar")

    # نترجم التصنيف
    for elem in programme.findall("category"):
        if elem.text:
            elem.text = translate_text(elem.text)
            elem.set("lang", "ar")

tree.write(output_file, encoding="utf-8", xml_declaration=True)

print(f"✅ تم إنشاء الملف المترجم: {output_file}")
