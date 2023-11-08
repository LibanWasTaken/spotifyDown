# Change date created to date modified

import os
import datetime
import ctypes

# Windows API constants
FILE_WRITE_ATTRIBUTES = 0x100
FILE_SHARE_READ = 0x1
OPEN_EXISTING = 3

# Replace with your folder path
folder_path = 'D:/new'

for filename in os.listdir(folder_path):
    if filename.endswith('.mp3'):
        file_path = os.path.join(folder_path, filename)
        
        # Convert modified time to FILETIME format
        modified_time = os.path.getmtime(file_path)
        filetime = int(modified_time * 10000000 + 116444736000000000)
        
        try:
            # Open the file for write attributes
            handle = ctypes.windll.kernel32.CreateFileW(
                file_path,
                FILE_WRITE_ATTRIBUTES,
                FILE_SHARE_READ,
                None,
                OPEN_EXISTING,
                0,
                None
            )
            
            # Set the new creation time
            ctypes.windll.kernel32.SetFileTime(
                handle,
                ctypes.byref(ctypes.c_longlong(filetime)),
                None,
                None
            )
            
            # Close the file handle
            ctypes.windll.kernel32.CloseHandle(handle)
            
            print(f"Changed creation time of '{filename}' to match modified time.")
        except Exception as e:
            print(f"Error changing creation time of '{filename}': {e}")
