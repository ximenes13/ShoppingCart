import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Themes
themes = {
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "entry_bg": "#ffffff",
        "entry_fg": "#000000",
        "button_bg": "#e0e0e0",
        "button_fg": "#000000"
    },
    "dark": {
        "bg": "#2e2e2e",
        "fg": "#ffffff",
        "entry_bg": "#3c3f41",
        "entry_fg": "#ffffff",
        "button_bg": "#444444",
        "button_fg": "#ffffff"
    }
}

current_theme = "light"
cart = {}
history = []

def add_cart():
    item = entry_item.get().strip()
    try:
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid price or quantity.")
        return

    if not item:
        messagebox.showerror("Error", "Item name is required.")
        return

    if item in cart:
        cart[item]['quantity'] += quantity
    else:
        cart[item] = {'price': price, 'quantity': quantity}

    load_action(f"Added {quantity} x {item} @€{price:.2f}")
    update_cart_display()

    entry_item.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_item.focus_set()

def remove_selected():
    remove_items = [item for item, var in check_vars.items() if var.get()]
    for item in remove_items:
        del cart[item]
        load_action(f"Removed {item} from cart.")
    update_cart_display()

def clear_cart():
    cart.clear()
    load_action("Cleared cart.")
    update_cart_display()

def load_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"[{timestamp}] {action}")
    update_history_display()

def update_cart_display():
    for widget in frame_cart.winfo_children():
        widget.destroy()

    global check_vars
    check_vars = {}

    total_price_cart = 0
    for item, details in cart.items():
        var = tk.BooleanVar()
        chk = tk.Checkbutton(frame_cart,
                             text=f"{item} - €{details['price']:.2f} x {details['quantity']}",
                             variable=var,
                             bg=themes[current_theme]["bg"],
                             fg=themes[current_theme]["fg"],
                             selectcolor=themes[current_theme]["bg"])
        chk.pack(anchor='w')
        check_vars[item] = var
        total_price_cart += details['price'] * details['quantity']

    label_total.config(text=f"Total: ${total_price_cart:.2f}")

def update_history_display():
    text_history.delete(1.0, tk.END)
    for entry in history:
        text_history.insert(tk.END, entry + "\n")

def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = themes[theme_name]

    root.configure(bg=theme["bg"])
    frame_input.configure(bg=theme["bg"])
    for widget in frame_input.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(bg=theme["bg"], fg=theme["fg"])
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=theme["entry_bg"], fg=theme["entry_fg"], insertbackground=theme["entry_fg"])
    for btn in [btn_add, btn_remove, btn_clear, dark_btn, light_btn]:
        btn.config(bg=theme["button_bg"], fg=theme["button_fg"],
                   activebackground=theme["button_bg"], activeforeground=theme["button_fg"])
    frame_cart.configure(bg=theme["bg"], fg=theme["fg"])
    for widget in frame_cart.winfo_children():
        if isinstance(widget, tk.Checkbutton):
            widget.configure(bg=theme["bg"], fg=theme["fg"], selectcolor=theme["bg"])
    label_total.configure(bg=theme["bg"], fg=theme["fg"])
    frame_history.configure(bg=theme["bg"], fg=theme["fg"])
    text_history.configure(bg=theme["entry_bg"], fg=theme["entry_fg"])
    frame_theme.configure(bg=theme["bg"])

# GUI Setup
root = tk.Tk()
root.title("Shopping Cart")

# Inputs
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack()

tk.Label(frame_input, text="Item:").grid(row=0, column=0)
entry_item = tk.Entry(frame_input)
entry_item.grid(row=0, column=1)

tk.Label(frame_input, text="Price:").grid(row=1, column=0)
entry_price = tk.Entry(frame_input)
entry_price.grid(row=1, column=1)

tk.Label(frame_input, text="Quantity:").grid(row=2, column=0)
entry_quantity = tk.Entry(frame_input)
entry_quantity.grid(row=2, column=1)

btn_add = tk.Button(frame_input, text="Add to Cart", command=add_cart)
btn_add.grid(row=3, columnspan=2, pady=5)

# Cart Display
frame_cart = tk.LabelFrame(root, text="Cart", padx=10, pady=10)
frame_cart.pack(fill="both", expand=True, padx=10, pady=5)

label_total = tk.Label(root, text="Total: €0.00", font=("Arial", 12))
label_total.pack()

btn_remove = tk.Button(root, text="Remove Selected", command=remove_selected)
btn_remove.pack(pady=2)

btn_clear = tk.Button(root, text="Clear Cart", command=clear_cart)
btn_clear.pack(pady=2)

# History
frame_history = tk.LabelFrame(root, text="History", padx=10, pady=10)
frame_history.pack(fill="both", expand=True, padx=10, pady=5)

text_history = tk.Text(frame_history, height=10)
text_history.pack()

# Theme switch buttons
frame_theme = tk.Frame(root, bg=themes[current_theme]["bg"])
frame_theme.pack(fill="x", padx=10, pady=10)


dark_btn = tk.Button(frame_theme, text="🌙", command=lambda: apply_theme("dark"))
dark_btn.grid(row=0, column=0, sticky="we", padx=5)

light_btn = tk.Button(frame_theme, text="☀️", command=lambda: apply_theme("light"))
light_btn.grid(row=0, column=1, sticky="we", padx=5)

apply_theme("light")  # Apply initial theme

root.mainloop()
