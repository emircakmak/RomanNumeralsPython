from tkinter import *
from tkinter import messagebox

def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for letter in roman.upper():
        if letter not in roman_values:
            raise ValueError("Invalid input: Only Roman numerals (I, V, X, L, C, D, M) are allowed")

    for letter in reversed(roman.upper()):
        value = roman_values.get(letter, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    if total > 4999:
        raise ValueError("Invalid Roman Numeral: Greater Than 4999")

    return total

def convert():
    roman_numeral = question_entry.get()
    try:
        integer = roman_to_integer(roman_numeral)
        result_label.config(text=f"Result: {integer}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))


window = Tk()
window.title("Roman Numerals")
window.geometry("500x700")

img = PhotoImage(file="romannumarels.png")
img_label = Label(image=img)
img_label.place(x=115, y=0)

question_label = Label(text="Enter Your Roman Number", font=('Helvetica', 12, 'bold'))
question_label.place(x=146, y=220)

question_entry = Entry(width=30, font=('Helvetica', 9, 'bold'))
question_entry.focus()
question_entry.place(x=145, y=256)

result_label = Label(text="Result: ", font=('Helvetica', 14, 'bold'))
result_label.place(x=185, y=380)

convert_button = Button(text="Convert", height=2, width=10, font=('Helvetica', 10, 'bold'), command=convert)
convert_button.place(x=200, y=290)

window.mainloop()