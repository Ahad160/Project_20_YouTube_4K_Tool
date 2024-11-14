import tkinter as tk
from tkinter import ttk


# Initialize the main application window
root = tk.Tk()
root.title("4K Download")

# Load the Azure theme
try:
    root.tk.call("source", r"E:\Codeing\Python Language\GUI\Azure-ttk-theme-main\Azure-ttk-theme-main\azure.tcl")  # Replace with the correct path to azure.tcl
    root.tk.call("set_theme", "light")  # Use "dark" for dark mode
except tk.TclError:
    print("Azure theme file not found. Please check the path to 'azure.tcl'.")

# Main label
label = ttk.Label(root, text="YouTube 4K Video Downloader")
label.pack(padx=20, pady=20)    

# Main label with extra bottom padding
label = ttk.Label(root, text="Enter YouTube Video link")
label.pack(padx=20, pady=(20, 0))  # Reduces bottom padding on the label

# Add a ttk entry box with top padding to add more spacing below the label
entry = ttk.Entry(root, width=30)
entry.pack(padx=20, pady=(10, 20))  # Adds top padding on the entry box

def Download_Event():
    Url=entry.get()
    

# Apply the style to the button
accent_button = ttk.Button(root, text="Download", style='Accent.TButton')
accent_button.pack(padx=20, pady=(10, 20))

# Run the application
root.mainloop()
