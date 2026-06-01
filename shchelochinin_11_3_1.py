from tkinter import *
from tkinter import messagebox

def solve():
    try:
        a1 = float(e_a1.get())
        b1 = float(e_b1.get())
        c1 = float(e_c1.get())

        a2 = float(e_a2.get())
        b2 = float(e_b2.get())
        c2 = float(e_c2.get())

        d = a1 * b2 - a2 * b1

        if d == 0:
            messagebox.showerror("Помилка", "Система не має єдиного розв'язку!")
            return

        x = (c1 * b2 - c2 * b1) / d
        y = (a1 * c2 - a2 * c1) / d

        lbl_result.config(text=f"x = {x:.2f}    y = {y:.2f}")

    except ValueError:
        messagebox.showerror("Помилка", "Введіть числа!")

def close():
    root.destroy()

root = Tk()
root.title("Розв'язання системи рівнянь")
root.geometry("300x140")

for i in range(5):
    root.grid_columnconfigure(i, weight=1)

e_a1 = Entry(root, width=5)
e_a1.grid(row=0, column=0, pady=5)

Label(root, text="x +").grid(row=0, column=1)

e_b1 = Entry(root, width=5)
e_b1.grid(row=0, column=2)

Label(root, text="y =").grid(row=0, column=3)

e_c1 = Entry(root, width=5)
e_c1.grid(row=0, column=4)

e_a2 = Entry(root, width=5)
e_a2.grid(row=1, column=0, pady=5)

Label(root, text="x +").grid(row=1, column=1)

e_b2 = Entry(root, width=5)
e_b2.grid(row=1, column=2)

Label(root, text="y =").grid(row=1, column=3)

e_c2 = Entry(root, width=5)
e_c2.grid(row=1, column=4)

lbl_result = Label(root, text="x = ?    y = ?")
lbl_result.grid(row=2, column=0, columnspan=5, pady=10)

Button(root, text="Обчислити", command=solve).grid(row=3, column=0, columnspan=2, pady=5)

Button(root, text="Закрити", command=close).grid(row=3, column=3, columnspan=2, pady=5)

root.mainloop()