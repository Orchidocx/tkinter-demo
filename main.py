import tkinter

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Tkinter GUI")
    window.minsize(width=500,height=300)

    # Label
    my_label = tkinter.Label(text="I am a label")

    # end statement
    window.mainloop()
