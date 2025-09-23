import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
import requests
import io

# رابط المصدر (غير متعلق بالملفات داخل الريبو)
SOURCE_URL = "https://raw.githubusercontent.com/ayoubboukous27/Bein-Sports-MENA-epg/main/epg_mapped_with_logos.xml"

OUTPUT_FILE = "epg_mapped_with_logos_ar.xml"

def translate_text(text):
    try:
        return GoogleTranslator(source="auto", target="ar").translate(text)
    except Exception as e:
        print(f"⚠️ خطأ أثناء الترجمة: {e}")
        return text

def main():
    print(f"⬇️ جاري تحميل الملف من {SOURCE_URL}")
    response = requests.get(SOURCE_URL)
    if response.status_code != 200:
        print("❌ فشل تحميل الملف من المصدر")
        return

    # قراءة XML من الذاكرة بدل ملف محلي
    tree = ET.parse(io.StringIO(response.text))
    root = tree.getroot()

    count = 0
    for programme in root.findall("programme"):
        for tag in ["title", "desc", "category"]:
            element = programme.find(tag)
            if element is not None and element.text:
                translated = translate_text(element.text)
                new_elem = ET.SubElement(programme, tag, {"lang": "ar"})
                new_elem.text = translated
                count += 1

    tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)
    print(f"✅ تم إنشاء {OUTPUT_FILE} مع {count} عنصر مترجم.")

if __name__ == "__main__":
    main()
