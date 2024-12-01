import tkinter as tk
from tkinter import ttk
from yt_dlp import YoutubeDL
from tkinter import filedialog


def YouTube_Download_Module(Url):
    Video_Settings= {
        'format': f'bestvideo[height<={selected_option.get()}]+bestaudio/best[height<=2160]',

        # 'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',

        'outtmpl': r'4K-V.%(ext)s',
    }
    with YoutubeDL(Video_Settings) as ydl:
        ydl.download([Url])


def Download_Event():
    
    User_URL=entry.get()
    YouTube_Download_Module(User_URL)
    # Main label with extra bottom padding
    label = ttk.Label(root, text="Patience, The Video is Downloading...",foreground="#ff8000")
    label.grid(row=0, column=0,padx=0, pady=(0,0))  # Reduces bottom padding on the label
    #Padx left-Right
    #pady up-down

    # Main label with extra bottom padding
    label = ttk.Label(root, text="Download Completed!",foreground="#006400")
    label.grid(row=0, column=0,padx=0, pady=(0,0))  # Reduces bottom padding on the label

#⭕ Audio Checkbuttons Function
def checkbutton_callback(var):
    if var.get():
        # Checkbutton is checked
        label.config(text="Checkbutton is checked")
    else:
        # Checkbutton is unchecked
        label.config(text="Checkbutton is unchecked")

def browse_folder():
    selected_folder = filedialog.askdirectory()
    target_folder_entry.delete(0, tk.END)
    target_folder_entry.insert(0, selected_folder)     
        

#               ---GUI MODE---
# Initialize the main application window
root = tk.Tk()
root.title("YouTube 4K Tool")
root.geometry("570x305")

# Load the Azure theme
try:
    root.tk.call("source", r"E:\Codeing\Python Language\Projects\Project_20_YouTube_4K_Tool\Theme\azure.tcl")  # Replace with the correct path to azure.tcl
    root.tk.call("set_theme", "light")  # Use "dark" for dark mode
except tk.TclError:
    print("Azure theme file not found. Please check the path to 'azure.tcl'.")

#⭕ Link Box
entry = ttk.Entry(root, width=50)
entry.grid(row=0, column=0, padx=0, pady=(2,5))

#⭕ Tab Design
notebook = ttk.Notebook(root, padding=(0, 0))
notebook.grid(row=1, column=0, sticky='w')
#⚪ Tab
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Formats")

#⚪ OptionMenu Design
label = ttk.Label(tab_2, text="Video Quality")
label.grid(row=2, column=0,padx=(0,0), pady=(0,1), sticky='w')
#⭕ OptionMenu
frame = ttk.Frame(tab_2, padding=(0, 0))
frame.grid(row=3, column=0, padx=(0,0), pady=(0,0), sticky="w")
option_menu_list = ["", "2160p (4K)", "1440p (2K)", "1080P","720p", "480p", "360p","240p","144p"]
selected_option = tk.StringVar(value=option_menu_list[1])
optionmenu = ttk.OptionMenu(frame, selected_option, *option_menu_list)
optionmenu.grid(row=2, column=0, padx=(0,0), pady=0, sticky="w")

#⚪ Audio Checkbuttons Function
var_0 = tk.BooleanVar(value=False)
var_1 = tk.BooleanVar(value=True)
#⭕ Audio Checkbuttons
check_1 = ttk.Checkbutton(tab_2, text="Audio", variable=var_1, command=lambda: checkbutton_callback(var_0))
check_1.grid(row=3, column=2, padx=(20,0), pady=(0,0), sticky="w")

#⭕ Targeted Folder Box
predefined_path = "C:/Users/YourUserName/Downloads"
# Target Folder Entry with pre-defined path
target_folder_entry = ttk.Entry(root, width=50)
target_folder_entry.insert(0, predefined_path)
target_folder_entry.grid(row=4, column=0, padx=0, pady=(5,0))

#⭕ Browse Button
browse_button = ttk.Button(root, text="Browse",command=browse_folder)
browse_button.grid(row=4, column=2, padx=(5,0), pady=(5,0), sticky="w")

#⭕ Download Button
accent_button = ttk.Button(root, text="Download", style='Accent.TButton',command=Download_Event)
accent_button.grid(row=4, column=3, padx=(5,0), pady=(5,0), sticky="w")



# Run the application
root.mainloop()