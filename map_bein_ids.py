import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import pytz
import re

# 🌐 خريطة القنوات والشعارات
CHANNELS = {
    "beIN Sports 1": {"id": "beINSports1.qa", "logo": "https://i.imgur.com/Vtk2cGI.png"},
    "beIN Sports 2": {"id": "beINSports2.qa", "logo": "https://i.imgur.com/vUJZSvs.png"},
    "beIN Sports 3": {"id": "beINSports3.qa", "logo": "https://i.imgur.com/UYSMao3.png"},
    "beIN Sports 4": {"id": "beINSports4.qa", "logo": "https://i.imgur.com/vwAgJNi.png"},
    "beIN Sports 5": {"id": "beINSports5.qa", "logo": "https://i.imgur.com/2Rha5aY.png"},
    "beIN Sports 6": {"id": "beINSports6.qa", "logo": "https://i.imgur.com/0wBdLYb.png"},
    "beIN Sports 7": {"id": "beINSports7.qa", "logo": "https://i.imgur.com/iODFwZi.png"},
    "beIN Sports":   {"id": "beINSports.qa",   "logo": "https://i.imgur.com/RLrMBlm.png"},
}

# 🌍 إعداد الوقت
timezone = pytz.timezone("Africa/Algiers")
now = datetime.now(timezone)

# 🏗️ إنشاء ملف XML
root = ET.Element("tv", generator="beIN Sports EPG", source="bein.com")

# إضافة القنوات
for name, info in CHANNELS.items():
    channel = ET.SubElement(root, "channel", id=info["id"])
    ET.SubElement(channel, "display-name").text = name
    ET.SubElement(channel, "icon", src=info["logo"])
    ET.SubElement(channel, "url").text = "https://bein.com"

# محاولة جلب البرامج الحقيقية من موقع beIN
url = "https://www.beinsports.com/en-mena/tv-guide"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # البحث عن البرامج لكل قناة
    for ch_name, ch_info in CHANNELS.items():
        program_items = soup.find_all('div', class_=re.compile(r'program-item|schedule-item', re.I))
        for i, program in enumerate(program_items[:8]):  # مثال: أول 8 برامج لكل قناة
            title_elem = program.find(['h3', 'h4', 'div'], class_=re.compile(r'title|name', re.I))
            desc_elem  = program.find(['p', 'div'], class_=re.compile(r'description|desc', re.I))
            time_elem  = program.find(['span', 'div'], class_=re.compile(r'time|hour', re.I))

            title = title_elem.get_text(strip=True) if title_elem else f"برنامج {i+1}"
            desc  = desc_elem.get_text(strip=True) if desc_elem else f"بث مباشر على {ch_name}"
            
            # إعداد وقت البدء والانتهاء
            if time_elem:
                t = time_elem.get_text(strip=True)
                try:
                    start_time = now.replace(hour=int(t[:2]), minute=int(t[3:5]), second=0)
                except:  # fallback
                    start_time = now + timedelta(hours=i)
            else:
                start_time = now + timedelta(hours=i)
            end_time = start_time + timedelta(hours=1, minutes=30)

            prog = ET.SubElement(root, "programme",
                                 start=start_time.strftime("%Y%m%d%H%M%S %z"),
                                 stop=end_time.strftime("%Y%m%d%H%M%S %z"),
                                 channel=ch_info["id"])
            ET.SubElement(prog, "title", lang="ar").text = title
            ET.SubElement(prog, "desc", lang="ar").text = desc
            ET.SubElement(prog, "category", lang="ar").text = "رياضة"

except Exception as e:
    print(f"خطأ في جلب البرامج الحقيقية: {e}")
    # إذا فشل، يمكن عمل برامج تجريبية
    for ch_name, ch_info in CHANNELS.items():
        for i in range(8):
            start_time = now + timedelta(hours=i)
            end_time = start_time + timedelta(hours=1, minutes=30)
            prog = ET.SubElement(root, "programme",
                                 start=start_time.strftime("%Y%m%d%H%M%S %z"),
                                 stop=end_time.strftime("%Y%m%d%H%M%S %z"),
                                 channel=ch_info["id"])
            ET.SubElement(prog, "title", lang="ar").text = f"برنامج تجريبي {i+1}"
            ET.SubElement(prog, "desc", lang="ar").text = f"بث مباشر على {ch_name}"
            ET.SubElement(prog, "category", lang="ar").text = "رياضة"

# حفظ XML
tree = ET.ElementTree(root)
tree.write("epg.xml", encoding="utf-8", xml_declaration=True)
print("✅ تم إنشاء EPG.xml مع البرامج الحقيقية أو التجريبية")
