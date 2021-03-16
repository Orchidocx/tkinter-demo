from tkinter import *
# import tkinter

if __name__ == '__main__':
    window = Tk()
    window.title("Tkinter GUI")
    window.minsize(width=500,height=300)

    # Label
    my_label = Label(text="I am a label", font=("Courier New", 20, "bold"))
    my_label.pack()
    my_label["text"] = "new text"   # changing the text
    my_label.config(text="newer text")  # another way to change text

    # Button
    button = Button(text="hello")

    # end statement
    window.mainloop()
