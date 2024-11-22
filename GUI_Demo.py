import tkinter as tk
from tkinter import ttk
from yt_dlp import YoutubeDL




#               ---GUI MODE---
# Initialize the main application window
root = tk.Tk()
root.title("4K Videos")

# Load the Azure theme
try:
    root.tk.call("source", r"E:\Codeing\Python Language\Projects\Project_20_YouTube_4K_Tool\Theme\azure.tcl")  # Replace with the correct path to azure.tcl
    root.tk.call("set_theme", "light")  # Use "dark" for dark mode
except tk.TclError:
    print("Azure theme file not found. Please check the path to 'azure.tcl'.")

# Main label
label = ttk.Label(root, text="YouTube 4K Video Downloader")
label.grid(padx=20, pady=20)    

# Main label with extra bottom padding
label = ttk.Label(root, text="Enter YouTube Video link")
label.grid(padx=20, pady=(20, 0))  # Reduces bottom padding on the label

# Add a ttk entry box with top padding to add more spacing below the label
entry = ttk.Entry(root, width=30)
entry.grid(padx=20, pady=(10, 20))  # Adds top padding on the entry box


# Apply the style to the button
accent_button = ttk.Button(root, text="Download", style='Accent.TButton',)
accent_button.grid(padx=20, pady=(10, 20))


# Main label with extra bottom padding
label = ttk.Label(root, text="Patience, The Video is Downloading...",foreground="#ff8000")
label.grid(padx=20, pady=(20,20))  # Reduces bottom padding on the label

# Main label with extra bottom padding
label = ttk.Label(root, text="Download Completed!",foreground="#006400")
label.grid(padx=20, pady=(0,0))  # Reduces bottom padding on the label


# Define a frame for the OptionMenu
frame = ttk.Frame(root, padding=(20, 10))
frame.grid(row=6, column=0, padx=20, pady=20, sticky="nsew")

# Create a list of options
option_menu_list = ["", "Option 1", "Option 2", "Option 3"]

# Create a StringVar to hold the selected value
selected_option = tk.StringVar(value=option_menu_list[1])

# Create the OptionMenu widget
optionmenu = ttk.OptionMenu(frame, selected_option, *option_menu_list)
optionmenu.grid(row=0, column=0, padx=50, pady=0, sticky="nsew")



# Run the application
root.mainloop()