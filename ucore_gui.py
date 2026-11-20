#!/data/data/com.termux/files/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import subprocess, os, threading, time

BG      = "#0d1117"
BG2     = "#161b22"
BORDER  = "#30363d"
BLUE    = "#5865f2"
GREEN   = "#57f287"
RED     = "#f85149"
TEXT    = "#e6edf3"
GRAY    = "#8b949e"

class UcoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ツcore v3.17")
        self.root.geometry("360x580")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.running = False
        self.muted   = False
        self.gain    = tk.DoubleVar(value=1.0)
        self.noise   = tk.DoubleVar(value=50)
        self.rec_proc = None

        self._build()

    # ───────── بناء الواجهة ─────────
    def _build(self):
        # ─ هيدر ─
        hdr = tk.Frame(self.root, bg=BG)
        hdr.pack(fill="x", pady=(24,0))
        tk.Label(hdr, text="ツ", font=("Segoe UI",40), bg=BG, fg=BLUE).pack()
        tk.Label(hdr, text="ツcore", font=("Segoe UI",22,"bold"),
                 bg=BG, fg=TEXT).pack()
        tk.Label(hdr, text="v3.17.0 — Discord Mic Enhancer",
                 font=("Segoe UI",9), bg=BG, fg=GRAY).pack(pady=(2,16))

        # ─ حالة ─
        status_frame = tk.Frame(self.root, bg=BG2, bd=0, highlightthickness=1,
                                highlightbackground=BORDER)
        status_frame.pack(fill="x", padx=20, pady=(0,16))
        inner = tk.Frame(status_frame, bg=BG2)
        inner.pack(pady=12)
        tk.Label(inner, text="الحالة", font=("Segoe UI",8), bg=BG2,
                 fg=GRAY).pack()
        self.dot_canvas = tk.Canvas(inner, width=14, height=14,
                                    bg=BG2, highlightthickness=0)
        self.dot_canvas.pack(side="left", padx=(0,6))
        self.dot = self.dot_canvas.create_oval(2,2,12,12, fill=RED, outline="")
        self.status_lbl = tk.Label(inner, text="متوقف",
                                   font=("Segoe UI",11,"bold"),
                                   bg=BG2, fg=RED)
        self.status_lbl.pack(side="left")

        # ─ أزرار تشغيل / إيقاف ─
        btn_row = tk.Frame(self.root, bg=BG)
        btn_row.pack(fill="x", padx=20, pady=(0,16))

        self.btn_on = tk.Button(btn_row, text="▶  تشغيل",
                                font=("Segoe UI",12,"bold"),
                                bg=BLUE, fg="white", relief="flat",
                                activebackground="#4752c4",
                                cursor="hand2", bd=0,
                                command=self.start)
        self.btn_on.pack(side="left", expand=True, fill="x",
                         ipady=10, padx=(0,8))

        self.btn_off = tk.Button(btn_row, text="■  إيقاف",
                                 font=("Segoe UI",12,"bold"),
                                 bg=BG2, fg=RED, relief="flat",
                                 activebackground="#21262d",
                                 cursor="hand2", bd=0, state="disabled",
                                 command=self.stop)
        self.btn_off.pack(side="left", expand=True, fill="x", ipady=10)

        # ─ تحكم بالمايك (يظهر بعد التشغيل) ─
        self.mic_frame = tk.Frame(self.root, bg=BG2, bd=0,
                                  highlightthickness=1,
                                  highlightbackground=BORDER)
        self.mic_frame.pack(fill="x", padx=20, pady=(0,16))
        self.mic_frame.pack_forget()   # مخفي في البداية

        tk.Label(self.mic_frame, text="🎙  تحكم بالمايك",
                 font=("Segoe UI",9,"bold"), bg=BG2, fg=GRAY).pack(
                 anchor="w", padx=16, pady=(10,8))

        # مستوى الصوت
        tk.Label(self.mic_frame, text="مستوى الصوت",
                 font=("Segoe UI",8), bg=BG2, fg=GRAY).pack(
                 anchor="w", padx=16)
        meter_bg = tk.Frame(self.mic_frame, bg="#21262d", height=10)
        meter_bg.pack(fill="x", padx=16, pady=(2,10))
        self.meter = tk.Frame(meter_bg, bg=GREEN, height=10, width=0)
        self.meter.place(x=0, y=0, relheight=1, width=0)

        # كسب
        self._slider_row(self.mic_frame, "الكسب", self.gain, 1, 10,
                         lambda v: self.gain_lbl.config(
                             text=f"{float(v):.1f}x"))
        self.gain_lbl = tk.Label(self.mic_frame, text="1.0x",
                                 font=("Segoe UI",8), bg=BG2, fg=GREEN)
        self.gain_lbl.pack(anchor="e", padx=16)

        # ضوضاء
        self._slider_row(self.mic_frame, "تخفيف الضوضاء", self.noise, 0, 100,
                         lambda v: self.noise_lbl.config(text=f"{int(float(v))}%"))
        self.noise_lbl = tk.Label(self.mic_frame, text="50%",
                                  font=("Segoe UI",8), bg=BG2, fg=GREEN)
        self.noise_lbl.pack(anchor="e", padx=16)

        # زر كتم
        self.mute_btn = tk.Button(self.mic_frame, text="🎙  كتم المايك",
                                  font=("Segoe UI",10,"bold"),
                                  bg="#f8514920", fg=RED, relief="flat",
                                  activebackground="#f8514930",
                                  cursor="hand2", bd=0,
                                  command=self.toggle_mute)
        self.mute_btn.pack(fill="x", padx=16, pady=(4,14), ipady=8)

        # ─ تعليمات ─
        info = tk.Frame(self.root, bg=BG2, bd=0, highlightthickness=1,
                        highlightbackground=BORDER)
        info.pack(fill="x", padx=20, pady=(0,10))
        steps = [
            "١. افتح Kiwi Browser",
            "٢. chrome://extensions",
            "٣. Developer mode → Load unpacked",
            "٤. اختر مجلد ucore_v3_17_0",
            "٥. افتح Discord → قناة صوتية",
        ]
        tk.Label(info, text="طريقة التثبيت",
                 font=("Segoe UI",8,"bold"), bg=BG2, fg=TEXT).pack(
                 anchor="w", padx=14, pady=(8,4))
        for s in steps:
            tk.Label(info, text=s, font=("Segoe UI",8),
                     bg=BG2, fg=GRAY, justify="right").pack(
                     anchor="w", padx=18)
        tk.Label(info, text="", bg=BG2).pack()

    def _slider_row(self, parent, label, var, mn, mx, cmd):
        row = tk.Frame(parent, bg=BG2)
        row.pack(fill="x", padx=16, pady=(4,0))
        tk.Label(row, text=label, font=("Segoe UI",8),
                 bg=BG2, fg=GRAY).pack(side="right")
        s = ttk.Scale(row, from_=mn, to=mx, variable=var,
                      orient="horizontal", command=cmd)
        s.pack(side="right", fill="x", expand=True, padx=(0,8))

    # ───────── تشغيل / إيقاف ─────────
    def start(self):
        self.running = True
        self._set_status(True)
        self.btn_on.config(state="disabled")
        self.btn_off.config(state="normal")
        self.mic_frame.pack(fill="x", padx=20, pady=(0,16),
                            before=self.mic_frame.master.winfo_children()[-1])
        # تشغيل المايك في الخلفية
        threading.Thread(target=self._start_mic, daemon=True).start()
        # تحريك العداد
        threading.Thread(target=self._animate_meter, daemon=True).start()

    def stop(self):
        self.running = False
        self._set_status(False)
        self.btn_on.config(state="normal")
        self.btn_off.config(state="disabled")
        self.mic_frame.pack_forget()
        try:
            subprocess.run(["termux-microphone-record", "-q"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=2)
        except: pass

    def _start_mic(self):
        try:
            self.rec_proc = subprocess.Popen(
                ["termux-microphone-record", "-l", "0", "-f", "/dev/null"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except: pass

    def _animate_meter(self):
        import random
        while self.running:
            w = random.randint(5, 85) if not self.muted else 0
            self.meter.place(width=int(self.mic_frame.winfo_width() * w / 100))
            time.sleep(0.12)
        self.meter.place(width=0)

    def toggle_mute(self):
        self.muted = not self.muted
        if self.muted:
            self.mute_btn.config(text="🔇  المايك مكتوم", bg=RED, fg="white")
            try:
                subprocess.run(["termux-microphone-record", "-q"],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=2)
            except: pass
        else:
            self.mute_btn.config(text="🎙  كتم المايك",
                                 bg="#f8514920", fg=RED)
            threading.Thread(target=self._start_mic, daemon=True).start()

    def _set_status(self, on):
        color = GREEN if on else RED
        text  = "يعمل" if on else "متوقف"
        self.dot_canvas.itemconfig(self.dot, fill=color)
        self.status_lbl.config(text=text, fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    # إزالة شريط العنوان إذا أردت مظهر تطبيق نظيف
    # root.overrideredirect(True)
    app = UcoreApp(root)

    # Style للـ slider
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Horizontal.TScale",
                    background=BG2, troughcolor="#30363d",
                    sliderlength=18, sliderrelief="flat")

    root.mainloop()
