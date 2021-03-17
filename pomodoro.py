from tkinter import *

PINK_LITE = "#f6dfeb"
PINK = "e4bad4"
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

    canvas = Canvas(width=202, height=224, bg=MINT, highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(102, 112, image=tomato_img)
    canvas.create_text(102, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
    canvas.pack()

    window.mainloop()
