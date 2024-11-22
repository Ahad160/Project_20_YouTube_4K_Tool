import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("OptionMenu Example")

# Set the theme
root.tk.call("source", r"E:\Codeing\Python Language\GUI\Azure-ttk-theme-main\Azure-ttk-theme-main\azure.tcl")
root.tk.call("set_theme", "dark")

# Define a frame for the OptionMenu
frame = ttk.Frame(root, padding=(20, 10))
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Create a list of options
option_menu_list = ["", "Option 1", "Option 2", "Option 3"]

# Create a StringVar to hold the selected value
selected_option = tk.StringVar(value=option_menu_list[1])

# Create the OptionMenu widget
optionmenu = ttk.OptionMenu(frame, selected_option, *option_menu_list)
optionmenu.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

# Run the Tkinter event loop
root.mainloop()
