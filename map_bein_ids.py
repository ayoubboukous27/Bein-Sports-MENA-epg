import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 3:
    print("Usage: python map_bein_ids.py input.xml output.xml")
    sys.exit(1)

src_file, out_file = sys.argv[1], sys.argv[2]

# 🟢 Map كامل لجميع قنوات beIN مع IDs الجديدة و روابط الشعارات
id_map = {
    "bein-sports-1": {"id": "beINSports1.qa", "logo": "https://i.imgur.com/Vtk2cGI.png"},
    "bein-sports-2": {"id": "beINSports2.qa", "logo": "https://i.imgur.com/vUJZSvs.png"},
    "bein-sports-3": {"id": "beINSports3.qa", "logo": "https://i.imgur.com/UYSMao3.png"},
    "bein-sports-4": {"id": "beINSports4.qa", "logo": "https://i.imgur.com/vwAgJNi.png"},
    "bein-sports-5": {"id": "beINSports5.qa", "logo": "https://i.imgur.com/2Rha5aY.png"},
    "bein-sports-6": {"id": "beINSports6.qa", "logo": "https://i.imgur.com/0wBdLYb.png"},
    "bein-sports-7": {"id": "beINSports7.qa", "logo": "https://i.imgur.com/iODFwZi.png"},
    "bein-sports-8": {"id": "beINSports8.qa", "logo": "https://i.imgur.com/RLrMBlm.png"},
    "bein-sports-9": {"id": "beINSports9.qa", "logo": "https://logos.fandom.com/wiki/BeIN_Sports_9"},

    # AFC
    "bein-sports-afc-1": {"id": "beINSportsAFC1.qa", "logo": "https://i.imgur.com/nk3JCpg.png"},
    "bein-sports-afc-2": {"id": "beINSportsAFC2.qa", "logo": "https://i.imgur.com/WITLbxq.png"},
    "bein-sports-afc-3": {"id": "beINSportsAFC3.qa", "logo": "https://i.imgur.com/ruRe9oj.png"},
    "bein-sports-afc":   {"id": "beINSportsAFC.qa", "logo": "https://i.imgur.com/HOj98bH.png"},
    
    # English
    "bein-sports-english-1": {"id": "beINSportsEnglish1.qa", "logo": "https://i.imgur.com/uqVwDrB.png"},
    "bein-sports-english-2": {"id": "beINSportsEnglish2.qa", "logo": "https://i.imgur.com/dWNbCyx.png"},
    "bein-sports-english-3": {"id": "beINSportsEnglish3.qa", "logo": "https://i.imgur.com/7bxQaJI.png"},
    
    # French
    "bein-sports-french-1": {"id": "beINSportsFrench1.qa", "logo": "https://i.imgur.com/tXqMkzA.png"},
    "bein-sports-french-2": {"id": "beINSportsFrench2.qa", "logo": "https://i.imgur.com/EG48QI7.png"},
    "bein-sports-french-3": {"id": "beINSportsFrench3.qa", "logo": "https://i.imgur.com/YbzCxeF.png"},
    
    # Max
    "bein-sports-max-1": {"id": "beINSportsMax1.qa", "logo": "https://i.imgur.com/FjWQjdy.png"},
    "bein-sports-max-2": {"id": "beINSportsMax2.qa", "logo": "https://i.imgur.com/5dBc5rn.png"},
    "bein-sports-max-3": {"id": "beINSportsMax3.qa", "logo": "https://i.imgur.com/ThcM2LE.png"},
    "bein-sports-max-4": {"id": "beINSportsMax4.qa", "logo": "https://i.imgur.com/j7osMfM.png"},
    "bein-sports-max-5": {"id": "beINSportsMax5.qa", "logo": "https://i.imgur.com/L6TvXAi.png"},
    "bein-sports-max-6": {"id": "beINSportsMax6.qa", "logo": "https://i.imgur.com/GHZHRPF.png"},
    
    # NBA & News
    "bein-sports-nba": {"id": "beINSportsNBA.qa", "logo": "https://i.imgur.com/QmSc6kh.png"},
    "bein-sports-news": {"id": "beINSportsNews.qa", "logo": "https://i.imgur.com/ZNjQzR5.png"}
}

tree = ET.parse(src_file)
root = tree.getroot()

# تعديل IDs داخل <programme>
for prog in root.findall("programme"):
    ch = prog.get("channel")
    if ch in id_map:
        prog.set("channel", id_map[ch]["id"])

# تعديل IDs و إضافة الشعارات داخل <channel>
for ch in root.findall("channel"):
    cid = ch.get("id")
    if cid in id_map:
        ch.set("id", id_map[cid]["id"])
        # إزالة أي أيقونة موجودة مسبقًا
        icon = ch.find("icon")
        if icon is not None:
            ch.remove(icon)
        # إضافة الأيقونة الجديدة
        ET.SubElement(ch, "icon", src=id_map[cid]["logo"])

tree.write(out_file, encoding="utf-8", xml_declaration=True)
print(f"✅ Saved mapped EPG with logos to {out_file}")
