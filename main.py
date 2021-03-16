from tkinter import *
# import tkinter

if __name__ == '__main__':
    window = Tk()
    window.title("Tkinter GUI")
    window.minsize(width=500,height=400)

    # Label
    my_label = Label(text="I am a label", font=("Courier New", 20, "bold"))
    my_label.pack()
    my_label["text"] = "new text"   # changing the text
    my_label.config(text="newer text")  # another way to change text

    # Button

    def button_click():
        print(f'You typed {u_input.get()}!')
        my_label.config(text=u_input.get())

    button = Button(text="click me", command=button_click)
    button.pack()

    # Entry (Input)
    u_input = Entry(width=10)
    u_input.pack()

    # Text (Entry)
    txt = Text(width=30, height=5)
    txt.focus() # focuses into text entry
    txt.insert(END, "Example of multi-line text entry.")
    txt.pack()

    # Spinbox
    spinbox = Spinbox(from_=0, to=10, width=10)
    spinbox.pack()

    # Scale
    scale = Scale(from_=1, to=10)
    scale.pack()

    # Checkbutton
    checked_state = IntVar()
    c_button = Checkbutton(text="isOn?", variable=checked_state)
    c_button.pack()

    # Radio Button
    radio_state = IntVar()
    r_button1 = Radiobutton(text="optionA", value=1, variable=radio_state)
    r_button2 = Radiobutton(text="optionB", value=2, variable=radio_state)
    r_button1.pack()
    r_button2.pack()

    # Listbox
    def listbox_used(evt):
        # Gets curr selection from listbox
        print(listbox.get(listbox.curselection()))
    listbox = Listbox(height=4)
    fruits = ["Apples", "Bananas", "Cherries", "Durian"]
    for fruit in fruits:
        listbox.insert(fruits.index(fruit), fruit)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()

    # end statement
    window.mainloop()
