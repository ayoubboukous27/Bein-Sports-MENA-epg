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
npm run grab --- --site=beinsports.com --output=guide_bein.xml --days=1

# 4) رجوع للمجلد الأصلي
cd ..

