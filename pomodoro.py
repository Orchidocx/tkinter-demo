import math
from tkinter import *

PINK_LITE = "#f6dfeb"
PINK = "#e4bad4"
RED_LITE = "#ff7171"
MINT_LITE = "#edffec"
MINT = "#caf7e3"
GREEN = "#00917c"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


def pomodoro():
    window = Tk()
    window.title("Pomodoro Timer")
    window.iconbitmap("tomato.ico")
    window.config(padx=100, pady=50, bg=MINT)

    def reset_timer():
        global reps
        window.after_cancel(timer)
        timer_label.config(text="Timer", fg=RED_LITE)
        canvas.itemconfig(timer_text, text="00:00")
        check_label.config(text="")
        reps = 0

    def start_timer():
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 8 == 0:
            count_down(long_break_sec)
            timer_label.config(text="Break!", fg=RED_LITE)
        elif reps % 2 == 1:
            count_down(work_sec)
            timer_label.config(text="Work!", fg=GREEN)
        else:
            count_down(short_break_sec)
            timer_label.config(text="Break!", fg=RED_LITE)

    def count_down(count):
        canvas.itemconfig(timer_text, text=f'{int(count/60)}:{count%60:02}')
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count - 1)
        else:
            check_label.config(text=f'{"✔" * math.floor(1+(reps/2))}')
            start_timer()

    timer_label = Label(text="Timer", fg=RED_LITE, bg=MINT, font=(FONT_NAME, 30, "bold"))
    check_label = Label(fg=RED_LITE, bg=MINT, font=(FONT_NAME, 15, "bold"))

    tomato_img = PhotoImage(file="tomato.png")
    canvas = Canvas(width=202, height=224, bg=MINT, highlightthickness=0)
    canvas.create_image(102, 112, image=tomato_img)
    timer_text = canvas.create_text(102, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

    start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
    reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)

    timer_label.grid(column=1, row=0)
    check_label.grid(column=1, row=3)
    canvas.grid(column=1, row=1)
    start_btn.grid(column=0, row=2)
    reset_btn.grid(column=2, row=2)

    window.mainloop()