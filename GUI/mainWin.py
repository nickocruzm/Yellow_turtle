import tkinter as tk

window = tk.Tk()
window.title("")

input_field_1 = tk.Entry(window)
input_field_2 = tk.Entry(window)

input_field_1 = tk.Entry(window)
input_field_2 = tk.Entry(window)

input_field_1.pack()
input_field_2.pack()

fred = tk.Button( window ,fg="red",bg="blue")
fred.config(fg="red",bg="blue")

fred.pack()



window.mainloop()