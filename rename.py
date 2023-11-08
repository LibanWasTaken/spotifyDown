# import os
# from mutagen.mp3 import MP3
# directory_path = "D:/testCopy"
# # directory_path = directory_path.replace("\\", "/")
# for filename in os.listdir(directory_path):
#     if filename.endswith(".mp3"): # Check if the file is an MP3 file
#         filepath = os.path.join(directory_path, filename) # Get the full file path
#         audio = MP3(filepath) # Read the metadata
#         title = str(audio["TIT2"])
#         artist = str(audio["TPE1"])
#         if "/" in artist:
#             artist = artist.replace("/", ", ")
#         if '"' in title:
#             title = title.replace('"', "'")
#         if '/' in title:
#             title = title.replace("/", ", ")   
#         new_filename = artist + " - " + title + ".mp3"
#         os.rename(filepath, os.path.join(directory_path, new_filename))
#         print(new_filename)

# I DIDNT NEED THESE (up) ANYMORE,

import os

folder_path = "D:/new" 

files = os.listdir(folder_path)

for file in files:
    if file.startswith("spotifydown.com - "):
        # Remove the prefix from the filename
        new_name = file[len("spotifydown.com - "):]
        
        # Construct the full paths for old and new filenames
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")
