import pyautogui
import pyperclip
import keyboard

# hold escape to escape
# https://spotifydown.com/ open this in browser
# make the browser the third icon in your uhh taskbar
# pre-set the download destination (download something else)
# install the packages
# fill these out ⬇️

# Start from:
count = 83

playlistLink = "https://open.spotify.com/playlist/02p8plM6b2M2IOhvJDKM4E?si=05a8f82b13a44ed6" # like this: https://open.spotify.com/playlist/02p8plMadsa6b0da
firstSongName = "We Are The People" # (rough) like this: We Are The People
totalCount = 87 # total number of songs: 123
outsidePos = [1564, 565] # uhh.. should be.. okay..?


def printPercentage(clipboard, attemptNo = 0):
    lines = clipboard.split('\n')
    
    # Assuming songName is on the third line and percentage is on the ninth line
    songName = lines[2].strip()  # Adjust if needed
    percentage = lines[8].strip()  # Adjust if needed

    print(f"{count}. {songName} - {percentage} - {attemptNo}")
    return percentage[:-1]


def printSongName(clipboard):
    lines = clipboard.split('\n')
    # songName = ' '.join(lines[1])
    songName = lines[2]
    print(f"{count}. {songName} 🟢")

def checkStatus(text, sleepDuration = 3):
    attempt = 0
    chance = 0
    while True:
        if keyboard.is_pressed('esc'):
            print("Escaped at count", count)
            exit(0)
        pyautogui.click(x=outsidePos[0], y=outsidePos[1])
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        clipboard_text = pyperclip.paste()
        # print(clipboard_text)
        if text not in clipboard_text:
            attempt += 1
            if text == "Download MP3":
                printPercentage(clipboard_text, attempt)
            else:
                print(count, "Not ready..", text, "-" , attempt)
            pyautogui.sleep(sleepDuration)
        else: 
        
            if text == "Download MP3":
                printSongName(clipboard_text)
            else:
                print(count, "Ready", text)
            attempt = 0
            return False
        if attempt > 80:
            # if text == "Download MP3":
            #     if str(printPercentage(clipboard_text)) > 50:
            #         chance += 1
            #     else:
            #      print(count, "🔴 Skipping", text)
            #      return True
            #     if chance > 1:
            #      print(count, "🔴 Skipping", text)
            #      return True
            # else:
                print(count, "🔴 Skipping", text)
                return True
            

def download():
    pyautogui.click(x=outsidePos[0], y=outsidePos[1])
    pyautogui.press('tab', presses=2) # Search

    pyautogui.typewrite(playlistLink) # paste link
    pyautogui.press('enter') # enter
    checkStatus(firstSongName, 1)
  
    pyautogui.click(x=outsidePos[0], y=outsidePos[1])
    pyautogui.press('tab', presses=(count + 1))
    pyautogui.press('enter') # enter
    pyautogui.sleep(2)

    pyautogui.press('home')
   

    skipThis =  checkStatus("Download MP3", 2)
    if not skipThis:
        skipThis = False
        pyautogui.click(x=outsidePos[0], y=outsidePos[1])
        pyautogui.press('tab', presses=2) # Download MP3
        pyautogui.press('enter') # enter
        pyautogui.sleep(3)

        # Name
        pyautogui.press('left')
        pyautogui.hotkey('ctrl', 'delete')
        pyautogui.hotkey('ctrl', 'delete')
        pyautogui.press('enter') # save
        pyautogui.sleep(1)

    # Resetting to homepage
    pyautogui.click(x=outsidePos[0], y=outsidePos[1])
    pyautogui.press('tab') # Logo / Home 
    pyautogui.press('enter')
    pyautogui.sleep(3)
    # Now at homepage

pyautogui.hotkey('win', '3') # open chrome
pyautogui.sleep(1)

while count <= totalCount:
    if ( playlistLink and firstSongName and totalCount and outsidePos): 
        print("Hold escape to escape")
        download()
        count += 1  
        if keyboard.is_pressed('esc'):
            print("Escaped at count", count)
            exit(0)
    else:
        print("Bzzt")
        break

