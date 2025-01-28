import tkinter as tk


def add_to_text(text, value):
    if text.get("1.0", tk.END).strip() == "Error":
        text.delete("1.0", tk.END)

    current_text = text.get("1.0", tk.END)
    current_text = current_text.strip("\n")
    text.delete("1.0", tk.END)
    text.insert("1.0", current_text + value)


def evaluate_calculation(text):
    try:
        current_text = text.get("1.0", tk.END)

        result = eval(current_text)
        
        text.delete("1.0", tk.END)
        text.insert("1.0", result)
    except:
        text.delete("1.0", tk.END)
        text.insert("1.0", "Error")


def clear_text(text):
    text.delete("1.0", tk.END)


def calculator():
    root = tk.Tk()
    root.geometry("350x350")
    root.title("Calculator")
    
    text = tk.Text(root, width=19, height=2, font=("Arial", 25))
    text.place(x=2, y=15) 
    button_1 = tk.Button(root, text="1", command=lambda: add_to_text(text, "1"), width=5, height=1, font=("Arial, 18"))
    button_1.place(x=5, y=100)
    button_2 = tk.Button(root, text="2", command=lambda: add_to_text(text, "2"), width=5, height=1, font=("Arial, 18"))
    button_2.place(x=91, y=100)
    button_3 = tk.Button(root, text="3", command=lambda: add_to_text(text, "3"), width=5, height=1, font=("Arial, 18"))
    button_3.place(x=177, y=100)
    button_plus = tk.Button(root, text="+", command=lambda: add_to_text(text, "+"), width=5, height=1, font=("Arial, 18"))
    button_plus.place(x=263, y=100)
    button_4 = tk.Button(root, text="4", command=lambda: add_to_text(text, "4"), width=5, height=1, font=("Arial, 18"))
    button_4.place(x=5, y=150)
    button_5 = tk.Button(root, text="5", command=lambda: add_to_text(text, "5"), width=5, height=1, font=("Arial, 18"))
    button_5.place(x=91, y=150)
    button_6 = tk.Button(root, text="6", command=lambda: add_to_text(text, "6"), width=5, height=1, font=("Arial, 18"))
    button_6.place(x=177, y=150)
    button_minus = tk.Button(root, text="-", command=lambda: add_to_text(text, "-"), width=5, height=1, font=("Arial, 18"))
    button_minus.place(x=263, y=150)
    button_7 = tk.Button(root, text="7", command=lambda: add_to_text(text, "7"), width=5, height=1, font=("Arial, 18"))
    button_7.place(x=5, y=200)
    button_8 = tk.Button(root, text="8", command=lambda: add_to_text(text, "8"), width=5, height=1, font=("Arial, 18"))
    button_8.place(x=91, y=200)
    button_9 = tk.Button(root, text="9", command=lambda: add_to_text(text, "9"), width=5, height=1, font=("Arial, 18"))
    button_9.place(x=177, y=200)
    button_asterisk = tk.Button(root, text="*", command=lambda: add_to_text(text, "*"), width=5, height=1, font=("Arial, 18"))
    button_asterisk.place(x=263, y=200)
    button_left_paranthesis = tk.Button(root, text="(", command=lambda: add_to_text(text, "("), width=5, height=1, font=("Arial, 18"))
    button_left_paranthesis.place(x=5, y=250)
    button_0 = tk.Button(root, text="0", command=lambda: add_to_text(text, "0"), width=5, height=1, font=("Arial, 18"))
    button_0.place(x=91, y=250)
    button_right_paranthesis = tk.Button(root, text=")", command=lambda: add_to_text(text, ")"), width=5, height=1, font=("Arial, 18"))
    button_right_paranthesis.place(x=177, y=250)
    button_slash = tk.Button(root, text="/", command=lambda: add_to_text(text, "/"), width=5, height=1, font=("Arial, 18"))
    button_slash.place(x=263, y=250)
    button_clear = tk.Button(root, text="C", command=lambda: clear_text(text), width=11, height=1, font=("Arial, 18"))
    button_clear.place(x=6, y=300)
    button_equal = tk.Button(root, text="=", command=lambda: evaluate_calculation(text), width=11, height=1, font=("Arial, 18"))
    button_equal.place(x=178, y=300)

    root.mainloop()


calculator()
