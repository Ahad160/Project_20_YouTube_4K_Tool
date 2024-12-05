import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def browse_folder():
    selected_folder = filedialog.askdirectory()
    target_folder_entry.delete(0, tk.END)
    target_folder_entry.insert(0, selected_folder)

# Set the pre-defined target folder path
predefined_path = "C:/Users/YourUserName/Downloads"

root = tk.Tk()
root.title("Target Folder Selector")

# Target Folder Entry with pre-defined path
target_folder_entry = ttk.Entry(root, width=50)
target_folder_entry.insert(0, predefined_path)
target_folder_entry.grid(row=0, column=0, padx=10, pady=10)

# Browse Button
browse_button = ttk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=1, padx=10, pady=10)

label = ttk.Label(root, text="Patience, Video is Downloading...",foreground="#ff8000",font=("-size", 10))
label.grid(padx=(0,0), pady=(0,0))  # Reduces bottom padding on the label

root.mainloop()