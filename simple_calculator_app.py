import tkinter as tk

# Creating a functionable mathematical operations
def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        result.set("Error")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        result.set("Error")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        result.set("Error")

def divide():
    try:
        if float(num2.get()) == 0:
            result.set("Error")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        result.set("Error")


root = tk.Tk()
root.title("Simple Calculator")

# Asking users to input a value for number 1
num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=0, column=0)
num1 = tk.Entry(root)
num1.grid(row=0, column=1)

# Asking the users to input a value for number 2
num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=1, column=0)
num2 = tk.Entry(root)
num2.grid(row=1, column=1)

# The computed value shows on the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0)
result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, state="readonly")
result_entry.grid(row=2, column=1)

# Buttons for operations
add_button = tk.Button(root, text="+", command=add) # "+" to add
add_button.grid(row=3, column=0)

subtract_button = tk.Button(root, text="-", command=subtract) # "-" to subtract
subtract_button.grid(row=3, column=1)

multiply_button = tk.Button(root, text="*", command=multiply) # "*" to multiply
multiply_button.grid(row=4, column=0)

divide_button = tk.Button(root, text="/", command=divide) # "/" to divide
divide_button.grid(row=4, column=1)

# Run the Tkinter event loop
root.mainloop()
