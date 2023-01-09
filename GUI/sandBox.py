import tkinter as tk

# +-------Log in--------+
window = tk.Tk()
window.title("new")

input_field_1 = tk.Entry(window)
input_field_2 = tk.Entry(window)

input_field_1 = tk.Entry(window)
input_field_2 = tk.Entry(window)

input_field_1.pack()
input_field_2.pack()

fred = tk.Button( window ,fg="red",bg="blue")
fred.config(fg="red",bg="blue")

fred.pack()


# +---------frames-----------+

root = tk.Tk()
root.title("Frame Example")
root.config(bg="grey47")

left_frame = tk.Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = tk.Frame(root, width=200, height=400)
right_frame.grid(row=0, column=1)
root.mainloop()