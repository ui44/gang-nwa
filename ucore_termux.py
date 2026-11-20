#!/data/data/com.termux/files/usr/bin/python3
import os, sys, time, subprocess, threading

# ألوان
R = "\033[0m"
B = "\033[1;34m"
G = "\033[1;32m"
Y = "\033[1;33m"
RD = "\033[1;31m"
C = "\033[1;36m"
W = "\033[1;37m"

running = False
muted = False
gain = 1.0
rec_proc = None

def clear():
    os.system("clear")

def header():
    print(f"""{C}
  ╔══════════════════════════════╗
  ║      ツ  c o r e  v3.17     ║
  ║   Discord Mic Enhancer       ║
  ╚══════════════════════════════╝{R}""")

def status_bar():
    state = f"{G}● يعمل{R}" if running else f"{RD}● متوقف{R}"
    mic   = f"{RD}🔇 مكتوم{R}" if muted else f"{G}🎙 مفعّل{R}"
    print(f"  الحالة: {state}   المايك: {mic}   الكسب: {Y}{gain}x{R}\n")

def main_menu():
    clear()
    header()
    status_bar()
    print(f"  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
    if not running:
        print(f"  {G}[1]{R} ▶  تشغيل")
    else:
        print(f"  {RD}[1]{R} ■  إيقاف")
    print(f"  {B}[2]{R} 🎙  تحكم بالمايك")
    print(f"  {Y}[3]{R} ⚙   الإعدادات")
    print(f"  {C}[4]{R} 📋  معلومات التثبيت")
    print(f"  {RD}[0]{R} ✖  خروج")
    print(f"  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
    return input(f"\n  {C}اختر:{R} ").strip()

def toggle_run():
    global running, rec_proc
    if not running:
        running = True
        print(f"\n  {G}✅ تم تشغيل ツcore!{R}")
        print(f"  {Y}افتح Discord وانضم لقناة صوتية{R}")
        # تشغيل تسجيل المايك في الخلفية إذا توفر
        try:
            rec_proc = subprocess.Popen(
                ["termux-microphone-record", "-l", "0", "-f", "/dev/null"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            print(f"  {G}🎙 المايك يعمل في الخلفية{R}")
        except:
            print(f"  {Y}⚠ ثبّت termux-api لتفعيل المايك الحقيقي{R}")
        time.sleep(2)
    else:
        running = False
        if rec_proc:
            try:
                subprocess.run(["termux-microphone-record", "-q"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                rec_proc = None
            except: pass
        print(f"\n  {RD}■ تم إيقاف ツcore{R}")
        time.sleep(1.5)

def mic_menu():
    global muted, gain
    while True:
        clear()
        header()
        status_bar()
        print(f"  {W}━━━ 🎙 تحكم بالمايك ━━━━━━━━━━━{R}")
        print(f"  {G}[1]{R} {'فك الكتم 🔊' if muted else 'كتم المايك 🔇'}")
        print(f"  {B}[2]{R} رفع الكسب   (الحالي: {Y}{gain}x{R})")
        print(f"  {B}[3]{R} خفض الكسب")
        print(f"  {Y}[4]{R} إعادة تعيين الكسب (1x)")
        print(f"  {RD}[0]{R} رجوع")
        print(f"  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
        ch = input(f"\n  {C}اختر:{R} ").strip()
        if ch == "1":
            muted = not muted
            state = "مكتوم" if muted else "مفعّل"
            try:
                # كتم المايك عبر termux-api
                if muted:
                    subprocess.run(["termux-microphone-record", "-q"],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    subprocess.Popen(["termux-microphone-record", "-l", "0", "-f", "/dev/null"],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except: pass
            print(f"\n  {G}✅ المايك الآن: {state}{R}")
            time.sleep(1.2)
        elif ch == "2":
            gain = round(min(gain + 0.5, 10.0), 1)
            print(f"\n  {G}✅ الكسب: {gain}x{R}")
            time.sleep(0.8)
        elif ch == "3":
            gain = round(max(gain - 0.5, 0.5), 1)
            print(f"\n  {G}✅ الكسب: {gain}x{R}")
            time.sleep(0.8)
        elif ch == "4":
            gain = 1.0
            print(f"\n  {G}✅ تم الإعادة: 1x{R}")
            time.sleep(0.8)
        elif ch == "0":
            break

def settings_menu():
    while True:
        clear()
        header()
        print(f"  {W}━━━ ⚙ الإعدادات ━━━━━━━━━━━━━━{R}")
        print(f"  {B}[1]{R} تحميل ملف الإضافة (ZIP)")
        print(f"  {Y}[2]{R} فتح مجلد الملفات")
        print(f"  {C}[3]{R} تحديث السكريبت")
        print(f"  {RD}[0]{R} رجوع")
        print(f"  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")
        ch = input(f"\n  {C}اختر:{R} ").strip()
        if ch == "1":
            print(f"\n  {Y}⬇ جاري التحميل...{R}")
            ret = os.system(
                "wget -q --show-progress "
                "https://github.com/ui44/gang-nwa/raw/main/ucore_v3_17_0.zip "
                "-O ~/storage/downloads/ucore_v3_17_0.zip && "
                "unzip -qo ~/storage/downloads/ucore_v3_17_0.zip "
                "-d ~/storage/downloads/ucore_v3_17_0/"
            )
            if ret == 0:
                print(f"  {G}✅ تم! المجلد: ~/storage/downloads/ucore_v3_17_0/{R}")
            else:
                print(f"  {RD}❌ فشل التحميل، تأكد من الإنترنت{R}")
            input(f"\n  {C}اضغط Enter للمتابعة...{R}")
        elif ch == "2":
            os.system("ls ~/storage/downloads/ 2>/dev/null || echo 'شغّل: termux-setup-storage'")
            input(f"\n  {C}اضغط Enter...{R}")
        elif ch == "3":
            print(f"\n  {Y}⬇ تحديث...{R}")
            os.system(
                "wget -q --show-progress "
                "https://raw.githubusercontent.com/ui44/gang-nwa/main/ucore_termux.py "
                "-O ~/ucore_termux.py"
            )
            print(f"  {G}✅ تم! أعد تشغيل السكريبت{R}")
            input(f"\n  {C}اضغط Enter...{R}")
        elif ch == "0":
            break

def info_menu():
    clear()
    header()
    print(f"""
  {W}━━━ 📋 طريقة التثبيت ━━━━━━━━━━{R}

  {Y}على Kiwi Browser / Yandex:{R}
  {G}1.{R} حمّل الملف من الإعدادات
  {G}2.{R} افتح chrome://extensions
  {G}3.{R} فعّل Developer mode
  {G}4.{R} Load unpacked ← ucore_v3_17_0
  {G}5.{R} افتح Discord ← قناة صوتية
  {G}6.{R} فعّل MIC ONLY 🎙

  {Y}رابط الموقع:{R}
  {C}https://ui44.github.io/gang-nwa{R}

  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}""")
    input(f"\n  {C}اضغط Enter للرجوع...{R}")

def main():
    # طلب إذن التخزين
    if not os.path.exists(os.path.expanduser("~/storage")):
        print(f"\n  {Y}⚠ شغّل أولاً: termux-setup-storage{R}\n")
        time.sleep(2)

    while True:
        ch = main_menu()
        if ch == "1":
            toggle_run()
        elif ch == "2":
            mic_menu()
        elif ch == "3":
            settings_menu()
        elif ch == "4":
            info_menu()
        elif ch == "0":
            clear()
            print(f"\n  {C}إلى اللقاء! ツ{R}\n")
            sys.exit(0)

if __name__ == "__main__":
    main()
