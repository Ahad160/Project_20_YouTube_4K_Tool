import tkinter as tk
import requests
from tkinter import ttk
from yt_dlp import YoutubeDL
from tkinter import filedialog
from PIL import Image, ImageTk
from io import BytesIO


#⭕ Thumnail Download Operations
def get_thumbnail_url(video_URL):
    ydl_opts = {"quiet": True, "skip_download": True}

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_URL, download=False)
        return info_dict.get("thumbnail")

def preview_thumbnail():
    global img_label, thumbnail_url

    video_url = Link_Box.get()
    if not video_url:
        return

    thumbnail_url = get_thumbnail_url(video_url)
    
    response = requests.get(thumbnail_url)
    img_data = Image.open(BytesIO(response.content))
    
    # Resize for preview
    img_data = img_data.resize((190, 130))
    img = ImageTk.PhotoImage(img_data)

    img_label.config(image=img)
    img_label.image = img

#⭕ Thumnail Download Function
def download_thumbnail():
    
    User_Path=target_folder_entry.get()

    video_url = Link_Box.get()
    if not video_url:
        return

    ydl_opts = {'skip_download': True, 'writethumbnail': True, 'outtmpl': rf'{User_Path}\Full_HD_Thumbnail.jpg'}

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    Log("Thumbnail")


#⭕ Video Download Operations
def YouTube_Download_Module(Url):
    User_Path=target_folder_entry.get()

    Video_Settings = {
        'format': (
            f'bestvideo[height<={selected_option.get().split(" ")[0].replace("p", "")}]+bestaudio/best[height<={selected_option.get().split(" ")[0].replace("p", "")}]'
            if globals().get("Audio_Option", True) else
            f'bestvideo[height<={selected_option.get().split(" ")[0].replace("p", "")}]'
        ),
        'outtmpl': rf'{User_Path}\4K-V.%(ext)s',
    }
    with YoutubeDL(Video_Settings) as ydl:
        ydl.download([Url])


#⭕ Console
def Log(Format):
    #⭕ Tab Design 2
    notebook = ttk.Notebook(root, padding=(2,5))
    notebook.grid(row=5, column=0, sticky='w')
    #⚪ Tab 2
    tab_3 = ttk.Frame(notebook)
    notebook.add(tab_3, text="Console")

    #⭕ Console Box Text 1
    label = ttk.Label(tab_3, text=f"Patience, {Format} is Downloading...",foreground="#ff8000",font=("-size", 10))
    label.grid(padx=(0,0), pady=(0,0))  # Reduces bottom padding on the label

    #⭕ Console Box Text 2
    label = ttk.Label(tab_3, text="Download Completed!",foreground="#8cc63f",font=("-size", 12, "-weight", "bold"))
    label.grid(padx=(0,0), pady=(0,0),sticky='w')  # Reduces bottom padding on the label


#⭕ Video Download Function
def Download_Event():
    
    User_URL=Link_Box.get()
    YouTube_Download_Module(User_URL)

    Log("Video")
    
    #Padx left-Right
    #pady up-down

#⭕ Audio Checkbuttons Function
def checkbutton_callback(var):
    global Audio_Option

    if var.get():
        # Checkbutton is checked
        Audio_Option=True
    else:
        # Checkbutton is unchecked
        Audio_Option=False


#⭕ Targeted Folder Path Function
def browse_folder():
    selected_folder = filedialog.askdirectory()
    target_folder_entry.delete(0, tk.END)
    target_folder_entry.insert(0, selected_folder)
    

# Initialize the main application window
root = tk.Tk()
root.title("YouTube 4K Tool")
root.geometry("570x260")
root.iconbitmap(r"E:\Codeing\Python Language\Projects\Project_20_YouTube_4K_Tool\YouTube_4K_Tool.ico")  # Replace with your icon path


# Load the Azure theme
try:
    root.tk.call("source", r"E:\Codeing\Python Language\Projects\Project_20_YouTube_4K_Tool\Theme\azure.tcl")  # Replace with the correct path to azure.tcl
    root.tk.call("set_theme", "dark")  # Use "dark" for dark mode
except tk.TclError:
    print("Azure theme file not found. Please check the path to 'azure.tcl'.")

#⭕ Link Box
Link_Box = ttk.Entry(root, width=50)
Link_Box.grid(row=0, column=0, padx=(2,0), pady=(1,5),sticky="w")
Link_Box.bind("<KeyRelease>", lambda e: preview_thumbnail())

#⭕ Tab Design
notebook = ttk.Notebook(root, padding=(2, 0))
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
option_menu_list = ["", "2160p (4K)", "1440p (2K)", "1080P (HD)","720p", "480p", "360p","240p","144p"]
selected_option = tk.StringVar(value=option_menu_list[1])
optionmenu = ttk.OptionMenu(frame, selected_option, *option_menu_list)
optionmenu.grid(row=2, column=0, padx=(0,0), pady=0, sticky="w")

#⚪ Audio Checkbuttons Function
var_0 = tk.BooleanVar(value=False)
var_1 = tk.BooleanVar(value=True)
#⭕ Audio Checkbuttons
check_1 = ttk.Checkbutton(tab_2, text="Audio", variable=var_1, command=lambda: checkbutton_callback(var_1))
check_1.grid(row=3, column=2, padx=(20,0), pady=(0,0), sticky="w")

#⭕ Thumbnail Download Button
accent_button = ttk.Button(root, text="Download Thumbnail", style='Accent.TButton',command=download_thumbnail)
accent_button.grid(row=1, column=0, padx=(220,0), pady=(60,0), sticky="w")

#⭕ Video Download Operations Design
img_label = tk.Label(root)
img_label.grid(row=0, column=1,rowspan=2, columnspan=3, padx=(0,0), pady=(2,0),sticky='e') 

#⭕ Targeted Folder Path Box
predefined_path = "C:/Users/PRO GADEGT/Downloads"
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