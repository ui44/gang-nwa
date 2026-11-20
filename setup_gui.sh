#!/data/data/com.termux/files/usr/bin/bash
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   ツcore GUI Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# تثبيت المتطلبات
echo "⬇ تثبيت المتطلبات..."
pkg install -y python tk x11-repo 2>/dev/null
pkg install -y termux-x11-nightly 2>/dev/null
pip install pillow 2>/dev/null

# تحميل السكريبت
echo "⬇ تحميل التطبيق..."
wget -q --show-progress \
  https://raw.githubusercontent.com/ui44/gang-nwa/main/ucore_gui.py \
  -O ~/ucore_gui.py

echo ""
echo "✅ تم! شغّل التطبيق بـ:"
echo ""
echo "  1️⃣  شغّل Termux:X11 من التطبيقات"
echo "  2️⃣  ثم نفّذ في Termux:"
echo ""
echo "     export DISPLAY=:0"
echo "     python3 ~/ucore_gui.py"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
