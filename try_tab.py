import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tab 2 Example")

# Set the theme
root.tk.call("source", r"E:\Codeing\Python Language\GUI\Azure-ttk-theme-main\Azure-ttk-theme-main\azure.tcl")
root.tk.call("set_theme", "dark")

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill="both",expand=True, padx=20, pady=20)

# Tab 1
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="Tab 1")

# Add content to Tab 1
label1 = ttk.Label(tab_1, text="Welcome to Tab 1")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = ttk.Entry(tab_1)
entry1.grid(row=1, column=0, padx=10, pady=10)

# Tab 2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")

# Add content to Tab 2
label2 = ttk.Label(tab_2, text="This is Tab 2")
label2.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

button1 = ttk.Button(tab_2, text="Button 1")
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = ttk.Button(tab_2, text="Button 2")
button2.grid(row=1, column=1, padx=10, pady=10)

# # Add an Entry widget in Tab 2
# entry = ttk.Entry(tab_2)
# entry.insert(0, "Type here...")
# entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# # Add a Button in Tab 2
# button = ttk.Button(tab_2, text="Click Me")
# button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

# # Make the rows and columns in Tab 2 expand dynamically
# for i in range(3):  # Adjust based on your layout
#     tab_2.rowconfigure(i, weight=1)
#     tab_2.columnconfigure(0, weight=1)

# Run the Tkinter event loop
root.mainloop()
