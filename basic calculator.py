import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to add characters to entry widget
def add_to_expression(char):
    entry.insert(tk.END, char)

# Function to clear entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for displaying expressions and results
entry = tk.Entry(root, width=20, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons and place them in the grid
for (text, row, column) in buttons:
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
              command=lambda char=text: add_to_expression(char)).grid(row=row, column=column, padx=5, pady=5)

# Clear button
tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear_entry).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Equals button
tk.Button(root, text='=', width=5, height=2, font=('Arial', 18), command=evaluate_expression).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Run the main loop
root.mainloop()