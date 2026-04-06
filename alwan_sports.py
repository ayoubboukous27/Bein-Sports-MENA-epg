from datetime import datetime, timedelta

channel_id = "alwan_sports"
channel_name = "Alwan Sports"
channel_icon = "https://raw.githubusercontent.com/ayoubboukous27/beIN-Sports-EPG-Worldwide/refs/heads/main/Logos/alwan-sports.png"

program_title = "البطولات الكروية مباشرة"
program_desc = (
    "نقل مباشر لجميع البطولات الكروية العالمية: دوري الأبطال والدوريات الأوروبية والعالمية."
)

start_date = datetime.utcnow()

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv generator-info-name="AlwanSportsEPG">\n'

xml += f'  <channel id="{channel_id}">\n'
xml += f'    <display-name>{channel_name}</display-name>\n'
xml += f'    <icon src="{channel_icon}"/>\n'
xml += '  </channel>\n'

for day in range(7):
    for hour in range(24):
        start = start_date + timedelta(days=day, hours=hour)
        stop = start + timedelta(hours=1)
        start_str = start.strftime("%Y%m%d%H%M%S") + " +0000"
        stop_str = stop.strftime("%Y%m%d%H%M%S") + " +0000"
        xml += f'  <programme start="{start_str}" stop="{stop_str}" channel="{channel_id}">\n'
        xml += f'    <title>{program_title}</title>\n'
        xml += f'    <desc>{program_desc}</desc>\n'
        xml += '  </programme>\n'

xml += '</tv>'

with open("alwan_sports_epg.xml", "w", encoding="utf-8") as f:
    f.write(xml)
