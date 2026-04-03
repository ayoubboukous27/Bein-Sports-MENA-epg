import xml.etree.ElementTree as ET

# 🟢 ملف EPG الحالي
input_file = "epg_mapped.xml"
# 🟢 الملف الناتج بعد تعديل الشعارات
output_file = "epg_mapped_with_logos.xml"

# 🟢 تعريف جميع القنوات مع روابط الشعارات
channels_logos = {
    "beINSports1.qa": "https://upload.wikimedia.org/wikipedia/commons/6/6c/1-HD.png",
    "beINSports2.qa": "https://upload.wikimedia.org/wikipedia/commons/5/51/2-HD.png",
    "beINSports3.qa": "https://upload.wikimedia.org/wikipedia/commons/f/fe/3-HD.png",
    "beINSports4.qa": "https://upload.wikimedia.org/wikipedia/commons/d/d1/4-HD.png",
    "beINSports5.qa": "https://upload.wikimedia.org/wikipedia/commons/f/f5/5-HD.png",
    "beINSports6.qa": "https://upload.wikimedia.org/wikipedia/commons/1/1d/6-HD.png",
    "beINSports7.qa": "https://upload.wikimedia.org/wikipedia/commons/2/27/7-HD.png",
    "beINSports8.qa": "https://upload.wikimedia.org/wikipedia/commons/c/cf/8-HD.png",
    "5C08D9D3-C713-4F1F-947E-87C761428B9B": "https://upload.wikimedia.org/wikipedia/commons/2/2f/9-HD.png",
    "beINSports.qa": "https://i.imgur.com/RLrMBlm.png",
    "beINSportsAFC1.qa": "https://i.imgur.com/nk3JCpg.png",
    "beINSportsAFC2.qa": "https://i.imgur.com/WITLbxq.png",
    "beINSportsAFC3.qa": "https://i.imgur.com/ruRe9oj.png",
    "beINSportsAFC.qa": "https://i.imgur.com/HOj98bH.png",
    "beINSportsEnglish1.qa": "https://i.imgur.com/uqVwDrB.png",
    "beINSportsEnglish2.qa": "https://i.imgur.com/dWNbCyx.png",
    "beINSportsEnglish3.qa": "https://i.imgur.com/7bxQaJI.png",
    "beINSports1.qa@France": "https://raw.githubusercontent.com/ayoubboukous27/beIN-Sports-EPG-Worldwide/refs/heads/main/Logos/bein-sports-1-programme-chaine-93.png",
    "beINSports2.qa@France": "https://raw.githubusercontent.com/ayoubboukous27/beIN-Sports-EPG-Worldwide/refs/heads/main/Logos/bein-sports-2-programme-chaine-15.png",
    "beINSports3.qa@France": "https://raw.githubusercontent.com/ayoubboukous27/beIN-Sports-EPG-Worldwide/refs/heads/main/Logos/bein-sports-3-programme-chaine-118.png",
    "beINSportsMax1.qa": "https://i.imgur.com/FjWQjdy.png",
    "beINSportsMax2.qa": "https://i.imgur.com/5dBc5rn.png",
    "beINSportsMax3.qa": "https://i.imgur.com/ThcM2LE.png",
    "beINSportsMax4.qa": "https://i.imgur.com/j7osMfM.png",
    "beINSportsMax5.qa": "https://i.imgur.com/L6TvXAi.png",
    "beINSportsMax6.qa": "https://i.imgur.com/GHZHRPF.png",
    "beINSportsNBA.qa": "https://i.imgur.com/QmSc6kh.png",
    "beINSportsNews.qa": "https://i.imgur.com/ZNjQzR5.png",
    "beINSportsPremium1.qa": "https://i.imgur.com/HELtOAC.png",
    "beINSportsPremium2.qa": "https://i.imgur.com/6HBpC0r.png",
    "beINSportsPremium3.qa": "https://i.imgur.com/2vxVwxF.png",
    "beINSportsXtra1.qa": "https://i.imgur.com/O9lTxQA.png",
    "beINSportsXtra2.qa": "https://i.imgur.com/08Y2CW1.png"
}

tree = ET.parse(input_file)
root = tree.getroot()

# تعديل الشعارات لجميع القنوات
for ch in root.findall("channel"):
    cid = ch.get("id")
    if cid in channels_logos:
        icon_elem = ch.find("icon")
        if icon_elem is None:
            icon_elem = ET.SubElement(ch, "icon")
        icon_elem.set("src", channels_logos[cid])

# حفظ الملف الجديد
tree.write(output_file, encoding="utf-8", xml_declaration=True)
print(f"✅ All logos updated and saved to {output_file}")
