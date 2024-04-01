import tkinter as tk
from tkinter import ttk

def on_button_click(button_text):
    print(f"Button clicked: {button_text}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Custom Button in List Example")

# Sample list of button texts
button_texts = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5"]

# Create and place a Treeview widget
tree = ttk.Treeview(root, columns=("buttons",), show="headings", height=len(button_texts))
tree.pack(pady=10)

# Add a custom column for buttons
tree.heading("buttons", text="Buttons")
tree.column("buttons", width=100)

# Configure ttk.Style to use custom style for buttons
style = ttk.Style()
style.configure("Custom.Treeview.Heading", anchor="w", font=("TkDefaultFont", 10, "bold"))
style.configure("Custom.Treeview.Cell", anchor="w", font=("TkDefaultFont", 10))

# Insert the custom button-like widgets into the Treeview
for text in button_texts:
    tree.insert("", tk.END, values=(text,))

# Function to handle button clicks
def button_click(event):
    item = tree.identify_row(event.y)
    col = tree.identify_column(event.x)
    if col == "#1":  # Check if the click is in the buttons column
        item_text = tree.item(item, "values")[0]
        on_button_click(item_text)

# Bind button clicks to the Treeview
tree.tag_configure("button", font=("TkDefaultFont", 10, "underline"), foreground="blue")
tree.tag_bind("button", "<Button-1>", button_click)

# Run the Tkinter event loop
root.mainloop()