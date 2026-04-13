import tkinter as tk


# ---------------- FUNCTIONS ----------------

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# ---------------- GUI SETUP ----------------

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.resizable(False, False)


# ---------------- DISPLAY ----------------

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill='both', ipadx=8, ipady=15)


# ---------------- BUTTON FRAME ----------------

frame = tk.Frame(root)
frame.pack()


# ---------------- BUTTON LAYOUT ----------------

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
]


# ---------------- CREATE BUTTONS ----------------

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')

    for btn in row:
        if btn == 'C':
            action = clear
        else:
            action = lambda x=btn: click(x)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 14),
            command=action,
            height=2,
            width=5
        ).pack(side='left', expand=True, fill='both')


# ---------------- EQUAL BUTTON ----------------

tk.Button(
    root,
    text='=',
    font=("Arial", 16),
    command=calculate,
    height=2
).pack(fill='both')


# ---------------- RUN APP ----------------

root.mainloop()
