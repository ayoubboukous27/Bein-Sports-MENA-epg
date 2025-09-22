# bein_epg.py
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import pytz

def generate_epg():
    print("بدء إنشاء EPG...")

    # إنشاء هيكل XML الأساسي
    root = ET.Element("tv", generator="beIN Sports EPG", source="bein.com")

    # قنوات beIN Sports
    channels = {
        "beIN SPORTS 1": "beIN1.mena",
        "beIN SPORTS 2": "beIN2.mena", 
        "beIN SPORTS 3": "beIN3.mena",
        "beIN SPORTS 4": "beIN4.mena",
        "beIN SPORTS 5": "beIN5.mena",
        "beIN SPORTS 6": "beIN6.mena",
        "beIN SPORTS 7": "beIN7.mena",
        "beIN SPORTS 8": "beIN8.mena",
        "beIN SPORTS 9": "beIN9.mena",
        "beIN SPORTS 10": "beIN10.mena",
        "beIN SPORTS 11": "beIN11.mena",
        "beIN SPORTS 12": "beIN12.mena",
        "beIN SPORTS NEWS": "beINNews.mena",
        "beIN SPORTS EN 1": "beINEng1.mena",
        "beIN SPORTS EN 2": "beINEng2.mena"
    }

    # إضافة القنوات إلى XML
    for name, channel_id in channels.items():
        channel = ET.SubElement(root, "channel", id=channel_id)
        ET.SubElement(channel, "display-name").text = name

    # إنشاء برامج تجريبية
    timezone = pytz.timezone("Africa/Algiers")
    now = datetime.now(timezone)

    for channel_id in channels.values():
        for i in range(8):  # 8 برامج لكل قناة
            start_time = now + timedelta(hours=i)
            end_time = start_time + timedelta(hours=1, minutes=30)

            programme = ET.SubElement(root, "programme",
                                      start=start_time.strftime("%Y%m%d%H%M%S %z"),
                                      stop=end_time.strftime("%Y%m%d%H%M%S %z"),
                                      channel=channel_id)

            ET.SubElement(programme, "title", lang="ar").text = f"برنامج تجريبي {i+1}"
            ET.SubElement(programme, "desc", lang="ar").text = f"هذا برنامج تجريبي للاختبار على القناة {channel_id}"
            ET.SubElement(programme, "category", lang="ar").text = "رياضة"

    # حفظ ملف XML
    tree = ET.ElementTree(root)
    tree.write("epg.xml", encoding="utf-8", xml_declaration=True)
    print("تم إنشاء ملف EPG بنجاح!")

if __name__ == "__main__":
    generate_epg()
