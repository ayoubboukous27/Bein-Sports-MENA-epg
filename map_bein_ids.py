import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 3:
    print("Usage: python map_bein_ids.py input.xml output.xml")
    sys.exit(1)

src_file, out_file = sys.argv[1], sys.argv[2]

# -------------------------------
# Mapping IDs
# -------------------------------
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

# -------------------------------
# Logos mapping (direct image URLs)
# -------------------------------
channels_logos = {
    "beINSports1.qa": "https://upload.wikimedia.org/wikipedia/commons/6/6c/1-HD.png",
    "beINSports2.qa": "https://upload.wikimedia.org/wikipedia/commons/5/51/2-HD.png",
    "beINSports3.qa": "https://upload.wikimedia.org/wikipedia/commons/f/fe/3-HD.png",
    "beINSports4.qa": "https://upload.wikimedia.org/wikipedia/commons/d/d1/4-HD.png",
    "beINSports5.qa": "https://upload.wikimedia.org/wikipedia/commons/f/f5/5-HD.png",
    "beINSports6.qa": "https://upload.wikimedia.org/wikipedia/commons/1/1d/6-HD.png",
    "beINSports7.qa": "https://upload.wikimedia.org/wikipedia/commons/2/27/7-HD.png",
    "beINSports8.qa": "https://upload.wikimedia.org/wikipedia/commons/c/cf/8-HD.png",
    "5C08D9D3-C713-4F1F-947E-87C761428B9B": "https://upload.wikimedia.org/wikipedia/commons/2/2f/9-HD.png"
}

# -------------------------------
# Parse XML
# -------------------------------
tree = ET.parse(src_file)
root = tree.getroot()

# Update IDs inside <programme>
for programme in root.findall("programme"):
    channel_id = programme.get("channel")
    if channel_id in id_map:
        programme.set("channel", id_map[channel_id])

# Update IDs inside <channel> and add logos
for channel in root.findall("channel"):
    cid = channel.get("id")
    # Update ID
    new_id = id_map.get(cid, cid)
    channel.set("id", new_id)

    # Remove existing <icon> if any
    for old_icon in channel.findall('icon'):
        channel.remove(old_icon)

    # Add <icon> if logo exists
    logo_url = channels_logos.get(new_id)
    if logo_url:
        icon = ET.Element('icon')
        icon.set('src', logo_url)
        channel.append(icon)

# Save XML
tree.write(out_file, encoding="utf-8", xml_declaration=True)
print(f"✅ Saved mapped EPG with logos to {out_file}")
