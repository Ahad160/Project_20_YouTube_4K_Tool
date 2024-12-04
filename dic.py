option_menu_list = ["", "2160p (4K)", "1440p (2K)", "1080P","720p", "480p", "360p (HD)","240p","144p"]

# Access the item and split by the parentheses
resolution = option_menu_list[8].split(" ")[0]  # Splits and takes the first part before space

print(resolution)
