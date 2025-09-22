import xml.etree.ElementTree as ET

# تعريف القنوات والشعارات
channels = [
    ("beINSports1.qa", "beIN Sports 1", "https://i.imgur.com/Vtk2cGI.png"),
    ("beINSports2.qa", "beIN Sports 2", "https://i.imgur.com/vUJZSvs.png"),
    ("beINSports3.qa", "beIN Sports 3", "https://i.imgur.com/UYSMao3.png"),
    ("beINSports4.qa", "beIN Sports 4", "https://i.imgur.com/vwAgJNi.png"),
    ("beINSports5.qa", "beIN Sports 5", "https://i.imgur.com/2Rha5aY.png"),
    ("beINSports6.qa", "beIN Sports 6", "https://i.imgur.com/0wBdLYb.png"),
    ("beINSports7.qa", "beIN Sports 7", "https://i.imgur.com/iODFwZi.png"),
    ("beINSports.qa", "beIN Sports", "https://i.imgur.com/RLrMBlm.png"),
    ("beINSportsAFC1.qa", "beIN Sports AFC 1", "https://i.imgur.com/nk3JCpg.png"),
    ("beINSportsAFC2.qa", "beIN Sports AFC 2", "https://i.imgur.com/WITLbxq.png"),
    ("beINSportsAFC3.qa", "beIN Sports AFC 3", "https://i.imgur.com/ruRe9oj.png"),
    ("beINSportsAFC.qa", "beIN Sports AFC", "https://i.imgur.com/HOj98bH.png"),
    ("beINSportsEnglish1.qa", "beIN Sports English 1", "https://i.imgur.com/uqVwDrB.png"),
    ("beINSportsEnglish2.qa", "beIN Sports English 2", "https://i.imgur.com/dWNbCyx.png"),
    ("beINSportsEnglish3.qa", "beIN Sports English 3", "https://i.imgur.com/7bxQaJI.png"),
    ("beINSportsFrench1.qa", "beIN Sports French 1", "https://i.imgur.com/tXqMkzA.png"),
    ("beINSportsFrench2.qa", "beIN Sports French 2", "https://i.imgur.com/EG48QI7.png"),
    ("beINSportsFrench3.qa", "beIN Sports French 3", "https://i.imgur.com/YbzCxeF.png"),
    ("beINSportsMax1.qa", "beIN Sports Max 1", "https://i.imgur.com/FjWQjdy.png"),
    ("beINSportsMax2.qa", "beIN Sports Max 2", "https://i.imgur.com/5dBc5rn.png"),
    ("beINSportsMax3.qa", "beIN Sports Max 3", "https://i.imgur.com/ThcM2LE.png"),
    ("beINSportsMax4.qa", "beIN Sports Max 4", "https://i.imgur.com/j7osMfM.png"),
    ("beINSportsMax5.qa", "beIN Sports Max 5", "https://i.imgur.com/L6TvXAi.png"),
    ("beINSportsMax6.qa", "beIN Sports Max 6", "https://i.imgur.com/GHZHRPF.png"),
    ("beINSportsNBA.qa", "beIN Sports NBA", "https://i.imgur.com/QmSc6kh.png"),
    ("beINSportsNews.qa", "beIN Sports News", "https://i.imgur.com/ZNjQzR5.png"),
]

# إنشاء XML
tv = ET.Element("tv")

for channel_id, display_name, logo in channels:
    channel = ET.SubElement(tv, "channel", id=channel_id)
    ET.SubElement(channel, "display-name").text = display_name
    ET.SubElement(channel, "icon", src=logo)
    ET.SubElement(channel, "url").text = "https://bein.com"

# حفظ الملف
tree = ET.ElementTree(tv)
tree.write("epg_mapped.xml", encoding="utf-8", xml_declaration=True)
