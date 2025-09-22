#!/bin/bash
set -e

# 1) سحب مشروع iptv-org/epg
if [ ! -d "epg" ]; then
  git clone --depth 1 https://github.com/iptv-org/epg.git
fi

cd epg

# 2) تثبيت المتطلبات
npm install

# 3) تشغيل الجلب لموقع beIN (غيّر الاسم لو مختلف)
npm run grab --- --site=beinsports.com --output=guide_bein.xml --days=2

# 4) رجوع للمجلد الأصلي
cd ..

# 5) تشغيل سكربت Python لتحويل IDs
python3 map_bein_ids.py epg/guide_bein.xml epg_mapped.xml
