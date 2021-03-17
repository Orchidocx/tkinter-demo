from tkinter import *
# import tkinter


def notes():
    window = Tk()
    window.title("Tkinter GUI")
    window.minsize(width=500, height=400)

    # Label
    my_label = Label(text="I am a label", font=("Courier New", 20, "bold"))
    my_label.pack()
    my_label["text"] = "new text"  # changing the text
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
    txt.focus()  # focuses into text entry
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

    # Pack, Place, Grid (TK Layout Managers)
    '''
    Pack - packing layout by stacking --> my_label.pack(side="right")
    Place - Precise Placement (x, y) --> my_label.place(x=0, y=0)
    Grid - Layout is relative to components --> my_label.grid(column=0, row=0) // my_button.grid(column=1, row=1)
    # CANNOT mix .grid and .pack

    '''

    # end statement
    window.mainloop()


def mi2Km():
    '''Miles to Kilometer converter'''




    u_input = Entry(text="0", width=10)
    u_input.grid(column=1, row=0)

    mile_label = Label(text="miles")
    mile_label.grid(column=2, row=0)

    equal_to_label = Label(text="is equal to")
    equal_to_label.grid(column=0, row=1)

    km_num_label = Label(text="0")
    km_num_label.grid(column=1, row=1)

    km_label = Label(text="km")
    km_label.grid(column=2, row=1)

    def convert_mi_km():
        km_num_label.config(text=f'{round(int(u_input.get()) * 1.609344,3)}')
    calc_btn = Button(text="calculate", command=convert_mi_km)
    calc_btn.grid(column=1, row=2)



if __name__ == '__main__':
    window = Tk()
    # window.minsize(width=400, height=300)
    mi2Km()
    window.mainloop()
