import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
import os

# اسم الملف الأصلي
INPUT_FILE = "epg_mapped_with_logos.xml"
# اسم الملف الناتج
OUTPUT_FILE = "epg_mapped_with_logos_ar.xml"

def translate_text(text):
    """ترجمة النص للغة العربية"""
    try:
        return GoogleTranslator(source="auto", target="ar").translate(text)
    except Exception as e:
        print(f"⚠️ خطأ أثناء الترجمة: {e}")
        return text  # لو فشل يترك النص كما هو

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ الملف {INPUT_FILE} غير موجود في المجلد.")
        return

    print(f"📂 جاري قراءة الملف: {INPUT_FILE}")
    tree = ET.parse(INPUT_FILE)
    root = tree.getroot()

    count = 0
    for programme in root.findall("programme"):
        for tag in ["title", "desc", "category"]:
            element = programme.find(tag)
            if element is not None and element.text:
                translated = translate_text(element.text)
                # إضافة عنصر جديد باللغة العربية
                new_elem = ET.SubElement(programme, tag, {"lang": "ar"})
                new_elem.text = translated
                count += 1

    tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)
    print(f"✅ تم إنشاء {OUTPUT_FILE} مع {count} عنصر مترجم.")

if __name__ == "__main__":
    main()
