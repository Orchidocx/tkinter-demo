from tkinter import *

PINK_LITE = "#f6dfeb"
PINK = "#e4bad4"
RED_LITE = "#ff7171"
MINT_LITE = "#edffec"
MINT = "#caf7e3"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def pomodoro():
    window = Tk()
    window.title("Pomodoro Timer")
    window.config(padx=100, pady=50, bg=MINT)

    timer_label = Label(text="Timer", fg=RED_LITE, bg=MINT, font=(FONT_NAME, 30, "bold"))
    check_label = Label(text="✔", fg=RED_LITE, bg=MINT, font=(FONT_NAME, 15, "bold"))

    tomato_img = PhotoImage(file="tomato.png")
    canvas = Canvas(width=202, height=224, bg=MINT, highlightthickness=0)
    canvas.create_image(102, 112, image=tomato_img)
    canvas.create_text(102, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

    start_btn = Button(text="Start", highlightthickness=0)
    reset_btn = Button(text="Reset", highlightthickness=0)

    timer_label.grid(column=1, row=0)
    check_label.grid(column=1, row=3)
    canvas.grid(column=1, row=1)
    start_btn.grid(column=0, row=2)
    reset_btn.grid(column=2, row=2)

    window.mainloop()
