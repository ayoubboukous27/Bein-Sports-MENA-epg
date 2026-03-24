import xml.etree.ElementTree as ET

# 🟢 ملف EPG الحالي
input_file = "epg_mapped.xml"
# 🟢 الملف الناتج بعد تعديل الشعارات
output_file = "epg_mapped_with_logos.xml"

# 🟢 تعريف جميع القنوات مع روابط الشعارات
channels_logos = {
    "beINSports1.qa": "https://i.imgur.com/Vtk2cGI.png",
    "beINSports2.qa": "https://i.imgur.com/vUJZSvs.png",
    "beINSports3.qa": "https://i.imgur.com/UYSMao3.png",
    "beINSports4.qa": "https://i.imgur.com/vwAgJNi.png",
    "beINSports5.qa": "https://i.imgur.com/2Rha5aY.png",
    "beINSports6.qa": "https://i.imgur.com/0wBdLYb.png",
    "beINSports7.qa": "https://i.imgur.com/iODFwZi.png",
    "beINSports8.qa": "https://i.imgur.com/CaFEyVn.png",
    "5C08D9D3-C713-4F1F-947E-87C761428B9B": "https://i.postimg.cc/3wh7xdLF/Picsart-26-02-28-15-43-43-590.png",
    "beINSports.qa": "https://i.imgur.com/RLrMBlm.png",
    "beINSportsAFC1.qa": "https://i.imgur.com/nk3JCpg.png",
    "beINSportsAFC2.qa": "https://i.imgur.com/WITLbxq.png",
    "beINSportsAFC3.qa": "https://i.imgur.com/ruRe9oj.png",
    "beINSportsAFC.qa": "https://i.imgur.com/HOj98bH.png",
    "beINSportsEnglish1.qa": "https://i.imgur.com/uqVwDrB.png",
    "beINSportsEnglish2.qa": "https://i.imgur.com/dWNbCyx.png",
    "beINSportsEnglish3.qa": "https://i.imgur.com/7bxQaJI.png",
    "beINSports1.qa@France": "https://raw.githubusercontent.com/ayoubboukous27/Event/refs/heads/main/Logos/bein1.png",
    "beINSports2.qa@France": "https://raw.githubusercontent.com/ayoubboukous27/Event/refs/heads/main/Logos/bein2.png",
    "beINSports3.qa@France": "https://raw.githubusercontent.com/ayoubboukous27/Event/refs/heads/main/Logos/bein3.png",
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
