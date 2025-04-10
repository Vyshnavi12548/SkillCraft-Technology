import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font="Arial 20", borderwidth=4, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font='Arial 18', relief=tk.RAISED, borderwidth=2)
        btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        btn.bind("<Button-1>", click)

root.mainloop()
