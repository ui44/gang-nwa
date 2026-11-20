#!/data/data/com.termux/files/usr/bin/bash

echo "================================"
echo "   ツcore v3.17.0 Downloader"
echo "================================"
echo ""

# تثبيت wget إذا مو موجود
pkg install wget -y -q 2>/dev/null

# مجلد التحميل
DEST="$HOME/storage/downloads/ucore_v3_17_0"
mkdir -p "$DEST"

echo "⬇ جاري التحميل..."
wget -q --show-progress \
  "https://github.com/ui44/gang-nwa/raw/main/ucore_v3_17_0.zip" \
  -O "$HOME/storage/downloads/ucore_v3_17_0.zip"

echo ""
echo "📦 جاري فك الضغط..."
pkg install unzip -y -q 2>/dev/null
unzip -q "$HOME/storage/downloads/ucore_v3_17_0.zip" -d "$DEST"

echo ""
echo "✅ تم! الملفات في:"
echo "   ~/storage/downloads/ucore_v3_17_0/"
echo ""
echo "الخطوة التالية:"
echo "  1. افتح Kiwi Browser أو Yandex Browser"
echo "  2. اكتب: chrome://extensions"
echo "  3. فعّل Developer mode"
echo "  4. اضغط Load unpacked"
echo "  5. اختر المجلد: Downloads/ucore_v3_17_0"
echo ""
echo "================================"
