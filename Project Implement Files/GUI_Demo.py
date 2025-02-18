import tkinter as tk
from tkinter import ttk
from yt_dlp import YoutubeDL



#               ---GUI MODE---
# Initialize the main application window
root = tk.Tk()
root.title("4K Videos")
root.geometry("500x400")


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


def On(selected_option):
    # global picked_option  # Declare the variable as global
    picked_option = selected_option
    # Main label with extra bottom padding
 


# Define a frame for the OptionMenu
frame = ttk.Frame(root, padding=(20, 10))
frame.grid(row=6, column=0, padx=20, pady=20, sticky="nsew")


# Create a list of options
option_menu_list = ["", "2160p (4K)", "1440p (2K)", "1080p (HD)","720p", "480p", "360p","240p","144p"]

# Create a StringVar to hold the selected value
selected_option = tk.StringVar(value=option_menu_list[1])

# Create the OptionMenu widget
optionmenu = ttk.OptionMenu(frame, selected_option, *option_menu_list,command=On)
optionmenu.grid(row=0, column=0, padx=50, pady=0, sticky="nsew")

#---------------------------------------------------------------------
def checkbutton_callback(var):
    if var.get():
        # Checkbutton is checked
        label.config(text="Checkbutton is checked")
    else:
        # Checkbutton is unchecked
        label.config(text="Checkbutton is unchecked")

# Create BooleanVars to track the state of each Checkbutton
var_0 = tk.BooleanVar(value=False)
var_1 = tk.BooleanVar(value=True)

# Create Checkbuttons
check_1 = ttk.Checkbutton(frame, text="Audio", variable=var_1, command=lambda: checkbutton_callback(var_0))
check_1.grid(row=0, column=5, padx=5, pady=10, sticky="nsew")

# Create a label to display the status
label = ttk.Label(frame, text="")
label.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")


# Input field
entry = ttk.Entry(root, width=40)
entry.pack(pady=10)
entry.insert(0, "Enter YouTube Link Here")

# Buttons
preview_btn = ttk.Button(root, text="Preview Thumbnail", )
preview_btn.pack(pady=5)

download_btn = ttk.Button(root, text="Download Thumbnail", )
download_btn.pack(pady=5)

# Thumbnail display
img_label = tk.Label(root)
img_label.pack()

# Status label
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)


# Run the application
root.mainloop()