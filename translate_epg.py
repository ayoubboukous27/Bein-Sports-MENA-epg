import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator

# اسم ملف الإدخال والإخراج
input_file = "epg_mapped_with_logos.xml"
output_file = "epg_mapped_with_logos_ar.xml"

# المترجم
translator = GoogleTranslator(source="auto", target="ar")

def translate_text(text):
    if not text:
        return ""
    try:
        return translator.translate(text)
    except Exception:
        return text

print("⏳ جاري الترجمة...")

tree = ET.parse(input_file)
root = tree.getroot()

for programme in root.findall("programme"):
    # نحذف النصوص القديمة
    for tag in ["title", "desc", "category"]:
        for element in programme.findall(tag):
            programme.remove(element)

    # نترجم النصوص ونضيفها بالعربية فقط
    original_title = programme.get("title") or ""
    title = translate_text(original_title)
    if title:
        t = ET.SubElement(programme, "title")
        t.set("lang", "ar")
        t.text = title

    # نترجم الوصف
    desc_elem = programme.find("desc")
    if desc_elem is not None and desc_elem.text:
        desc = translate_text(desc_elem.text)
        d = ET.SubElement(programme, "desc")
        d.set("lang", "ar")
        d.text = desc

    # نترجم التصنيف
    cat_elem = programme.find("category")
    if cat_elem is not None and cat_elem.text:
        cat = translate_text(cat_elem.text)
        c = ET.SubElement(programme, "category")
        c.set("lang", "ar")
        c.text = cat

# حفظ الملف الجديد
tree.write(output_file, encoding="utf-8", xml_declaration=True)

print(f"✅ تم إنشاء الملف المترجم: {output_file}")
