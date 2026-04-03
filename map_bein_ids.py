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

# 🟢 Logos mapping
channels_logos = {
    "beINSports1.qa": "https://commons.wikimedia.org/wiki/File:1-HD.png",
    "beINSports2.qa": "https://commons.wikimedia.org/wiki/File:2-HD.png",
    "beINSports3.qa": "https://commons.wikimedia.org/wiki/File:3-HD.png",
    "beINSports4.qa": "https://commons.wikimedia.org/wiki/File:4-HD.png",
    "beINSports5.qa": "https://commons.wikimedia.org/wiki/File:5-HD.png",
    "beINSports6.qa": "https://commons.wikimedia.org/wiki/File:6-HD.png",
    "beINSports7.qa": "https://commons.wikimedia.org/wiki/File:7-HD.png",
    "beINSports.qa": "https://i.imgur.com/RLrMBlm.png"
}

tree = ET.parse(src_file)
root = tree.getroot()

# -------------------------------
# Update IDs inside <programme>
# -------------------------------
for programme in root.findall("programme"):
    channel_id = programme.get("channel")
    if channel_id in id_map:
        programme.set("channel", id_map[channel_id])

# -------------------------------
# Update IDs inside <channel> and add logos
# -------------------------------
for channel in root.findall("channel"):
    cid = channel.get("id")
    # Update ID
    if cid in id_map:
        new_id = id_map[cid]
        channel.set("id", new_id)
    else:
        new_id = cid

    # Remove existing <icon> if any
    for old_icon in channel.findall('icon'):
        channel.remove(old_icon)

    # Add <icon> if logo exists
    logo_url = channels_logos.get(new_id)
    if logo_url:
        icon = ET.Element('icon')
        icon.set('src', logo_url)
        channel.append(icon)

tree.write(out_file, encoding="utf-8", xml_declaration=True)
print(f"✅ Saved mapped EPG with logos to {out_file}")
