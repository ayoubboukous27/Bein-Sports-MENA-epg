import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 3:
    print("Usage: python map_bein_ids.py input.xml output.xml")
    sys.exit(1)

src_file, out_file = sys.argv[1], sys.argv[2]

# 🟢 Change this mapping according to the IDs from iptv-org/epg
id_map = {
    "bein-sports-1": "beINSports1.qa",
    "bein-sports-2": "beINSports2.qa",
    "bein-sports-3": "beINSports3.qa",
    "bein-sports-4": "beINSports4.qa",
    "bein-sports-5": "beINSports5.qa",
    "bein-sports-6": "beINSports6.qa",
    "bein-sports-7": "beINSports7.qa",
    "bein-sports-8": "beINSports.qa"
}

tree = ET.parse(src_file)
root = tree.getroot()

# Update IDs inside <programme>
for programme in root.findall("programme"):
    channel_id = programme.get("channel")
    if channel_id in id_map:
        programme.set("channel", id_map[channel_id])

# Update IDs inside <channel>
for channel in root.findall("channel"):
    cid = channel.get("id")
    if cid in id_map:
        channel.set("id", id_map[cid])

tree.write(out_file, encoding="utf-8", xml_declaration=True)
print(f"✅ Saved mapped EPG to {out_file}")
