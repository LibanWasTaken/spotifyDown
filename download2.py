import pyautogui
import pyperclip
import keyboard

# hold escape to escape

# Start from:
count = 22

# playlistLink = "https://open.spotify.com/playlist/02p8plM6b2M2IOhvJDKM4E?si=061875beb2f54013"
playlistLink = "https://open.spotify.com/playlist/02p8plM6b2M2IOhvJDKM4E?si=af7be73e453e40da"
firstSongName = "We Are The People"
totalCount = 71
outsidePos = [1564, 565]


def checkStatus(text, sleepDuration = 3):
    attempt = 0
    pyautogui.sleep(sleepDuration)

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
            print(count, "Not ready..", text, "-" , attempt)
            pyautogui.sleep(sleepDuration)
        else: 
            print(count, "Ready", text)
            break  
        if attempt > 50:
            print(count, "🔴 ERROR", text)
            break  

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
    checkStatus("Download MP3", 2)
    
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
    pyautogui.press('tab', presses=3) 
    pyautogui.press('enter') # Another song

    pyautogui.sleep(5)
    # Now at homepage


pyautogui.hotkey('win', '3')# open chrome
pyautogui.sleep(1)

while count <= totalCount:
    download()
    # break
    print(count)
    count += 1  
    if keyboard.is_pressed('esc'):
        print("Escaped at count", count)
        exit(0)
