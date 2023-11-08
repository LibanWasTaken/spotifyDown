# Change date modified to whatever:

import os
from datetime import datetime
mp3_file_path = "D:/new/PHOENIX.mp3"
current_time = os.path.getmtime(mp3_file_path)
current_datetime = datetime.utcfromtimestamp(current_time)
print("Current last modified time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
new_datetime_str = input("Enter new last modified time (YYYY-MM-DD HH:MM:SS): ")
new_datetime = datetime.strptime(new_datetime_str, "%Y-%m-%d %H:%M:%S")
new_time = new_datetime.timestamp()
os.utime(mp3_file_path, (current_time, new_time))
print("Last modified time has been updated to:", new_datetime_str)
# 2023-04-19 15:30:59
print(current_time)