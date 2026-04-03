#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

in_file = sys.argv[1]  # epg_mapped.xml
out_file = sys.argv[2]  # epg_mapped_ids.xml

# تعريف كل القنوات وربط اسمها بالمعرف الرسمي
id_map = {
    "beIN SPORTS 1 Australia": "beINSports1.qa@Australia",
    "beIN SPORTS 2 Australia": "beINSports2.qa@Australia",
    "beIN SPORTS 3 Australia": "beINSports3.qa@Australia",
    "beIN SPORTS 1 France": "beINSports1.qa@France",
    "beIN SPORTS 2 France": "beINSports2.qa@France",
    "beIN SPORTS 3 France": "beINSports3.qa@France",
    "beIN SPORTS MAX 4 France": "beINSportsMax4.qa@France",
    "beIN SPORTS MAX 5 France": "beINSportsMax5.qa@France",
    "beIN SPORTS MAX 6 France": "beINSportsMax6.qa@France",
    "beIN SPORTS MAX 7 France": "beINSportsMax7.qa@France",
    "beIN SPORTS MAX 8 France": "beINSportsMax8.qa@France",
    "beIN SPORTS MAX 9 France": "beINSportsMax9.qa@France",
    "beIN SPORTS MAX 10 France": "beINSportsMax10.qa@France",
    "beIN SPORTS 3 USA": "beINSports3.qa@USA",
    "beIN SPORTS 4 USA": "beINSports4.qa@USA",
    "beIN SPORTS 5 USA": "beINSports5.qa@USA",
    "beIN SPORTS 6 USA": "beINSports6.qa@USA",
    "beIN SPORTS 7 USA": "beINSports7.qa@USA",
    "beIN SPORTS 8 USA": "beINSports8.qa@USA",
    "beIN SPORTS Malaysia": "beINSports1.qa@Malaysia",
    "beIN 4K Qatar": "beIN4K.qa",
    "beIN SPORTS Qatar": "beINSports.qa",
    "beIN SPORTS 1 Qatar": "beINSports1.qa",
    "beIN SPORTS 2 Qatar": "beINSports2.qa",
    "beIN SPORTS 3 Qatar": "beINSports3.qa",
    "beIN SPORTS 4 Qatar": "beINSports4.qa",
    "beIN SPORTS 5 Qatar": "beINSports5.qa",
    "beIN SPORTS 6 Qatar": "beINSports6.qa",
    "beIN SPORTS 7 Qatar": "beINSports7.qa",
    "beIN SPORTS 8 Qatar": "beINSports8.qa",
    "beIN SPORTS 9 Qatar": "beINSports9.qa",
    "beIN SPORTS AFC Qatar": "beINSportsAFC.qa",
    "beIN SPORTS AFC 1 Qatar": "beINSportsAFC1.qa",
    "beIN SPORTS AFC 2 Qatar": "beINSportsAFC2.qa",
    "beIN SPORTS AFC 3 Qatar": "beINSportsAFC3.qa",
    "beIN SPORTS Español Qatar": "beINSportsenEspanol.qa",
    "beIN SPORTS MAX 1 Qatar": "beINSportsMax1.qa",
    "beIN SPORTS MAX 2 Qatar": "beINSportsMax2.qa",
    "beIN SPORTS MAX 3 Qatar": "beINSportsMax3.qa",
    "beIN SPORTS MAX 4 Qatar": "beINSportsMax4.qa",
    "beIN SPORTS MAX 5 Qatar": "beINSportsMax5.qa",
    "beIN SPORTS MAX 6 Qatar": "beINSportsMax6.qa",
    "beIN SPORTS NBA Qatar": "beINSportsNBA.qa",
    "beIN SPORTS NEWS Qatar": "beINSportsNews.qa",
    "beIN SPORTS XTRA 1 Qatar": "beINSportsXtra1.qa",
    "beIN SPORTS XTRA 2 Qatar": "beINSportsXtra2.qa",
    "beIN SPORTS USA": "beINSportsUSA.us",
    "beIN SPORTS XTRA USA": "beINSPORTSXTRA.us",
    "beIN SPORTS XTRA ñ USA": "beINSPORTSXTRAenEspanol.us",
    "beIN SPORTS 9": "5C08D9D3-C713-4F1F-947E-87C761428B9B",
    "beIN SPORTS 1": "7836FEA9-6B39-4A1A-8352-DC5FCB97A16C",
    "beIN SPORTS 2 EN": "846C79D6-18F8-4A4D-ACFA-2C18DCCB6398",
    "beIN SPORTS 1 EN": "8C1EC4FC-35E6-4866-A75D-37FCFAE18839",
    "beIN SPORTS 1 FR": "93000494-0DF8-4107-AF0E-1C99D3DBB2EC",
    "beIN SPORTS 2 FR": "9B969275-E59C-4DD1-8FCA-8B01EAE04909",
    "beIN SPORTS 3": "7C714598-E7ED-4B0F-8BD1-E8E80D473922",
    "beIN SPORTS XTRA 3": "CDF1A4C8-26DD-4C33-A239-F729A3B09295",
    "beIN SPORTS 2": "DDFC8C16-6363-4A2C-AE66-2CE357DBC28E",
    "BEINC": "5ED9E1C4-BEF4-4AC2-8F90-28B3DCA26375",
    "BEINS8C": "520D107A-71D4-4CB7-B141-1C6B089A7FFC",
    "BEINSSC": "5824C394-7211-4004-AC46-35BD58B9D1EE",
    "beIN SPORTS": "A31EDF08-2A80-4D1F-9016-43A9C6138255",
    "beIN SPORTS": "B76EB90E-0657-4D61-9265-68ADA92E34CD"
}

tree = ET.parse(in_file)
root = tree.getroot()

# تحديث معرفات القنوات
for channel in root.findall('channel'):
    display = channel.find('display-name')
    if display is not None:
        name = display.text.strip()
        if name in id_map:
            channel.set('id', id_map[name])

# حفظ الملف المعدل
tree.write(out_file, encoding='utf-8', xml_declaration=True)
print(f"Mapped IDs saved to {out_file}")
