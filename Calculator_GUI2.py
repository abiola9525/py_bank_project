import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Colorful Calculator")

# Create the entry field
entry = tk.Entry(window, width=24, font=('Arial', 20), borderwidth=5, bg='#B9D9EB', fg='#262626')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button functions
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equals():
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        entry.insert(0, f_num / float(second_number))

# Create the button widgets
button_1 = tk.Button(window, text="1", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=35, pady=20, bg='#FBE8A6', font=('Arial', 16), command=lambda: button_click(0))
button_add = tk.Button(window, text="+", padx=34, pady=20, bg='#FD8E72', font=('Arial', 16), command=button_add)
button_subtract = tk.Button(window, text="-", padx=38, pady=20, bg='#FD8E72', font=('Arial', 16), command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=38, pady=20, bg='#FD8E72', font=('Arial', 16), command=button_multiply)
button_divide = tk.Button(window, text="/", padx=38, pady=20, bg='#FD8E72', font=('Arial', 16), command=button_divide)
button_equals = tk.Button(window, text="=", padx=80, pady=20, bg='#28B3A3', font=('Arial', 16), command=button_equals)
button_clear = tk.Button(window, text="C", padx=34, pady=20, bg='#FBE8A6', font=('Arial', 16), command=button_clear)

# Put the buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1)
button_equals.grid(row=5, column=2)

button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)

# Run the main loop
window.mainloop()


