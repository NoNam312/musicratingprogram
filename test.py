import tkinter as tk

def on_selection_change(selection):
    print("Selected:", selection)

root = tk.Tk()
root.geometry("300x200")

options = ["Option 1", "Option 2", "Option 3"]
option_var = tk.StringVar(root)
option_var.set(options[0])

# OptionMenu Button Style
option_button_style = {'bg': 'lightblue', 'fg': 'black'}

# OptionMenu Menu Style
option_menu_style = {'bg': 'lightyellow', 'fg': 'blue'}

# Create the OptionMenu
option_menu = tk.OptionMenu(root, option_var, *options, command=on_selection_change)
option_menu.config(**option_button_style)  # Apply style to the OptionMenu button
option_menu["menu"].config(**option_menu_style)  # Apply style to the OptionMenu menu

option_menu.pack(pady=20)

root.mainloop()