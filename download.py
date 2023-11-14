import pyautogui
import pyperclip

# https://spotifydown.com/
# zoom out to 50%

count = 1
scroll = 0

playlistLink = "https://open.spotify.com/playlist/02p8plM6b2M2IOhvJDKM4E?si=061875beb2f54013"
firstSongName = "We Are The People"
# totalCount = 71
totalCount = 30
maxTrackPerPage = 16
xPosition = 1183 #starting track x position
yPosition = 395 #starting track y position
yPosition2 = 435 #2nd track y position
newYPos = 238 # after pressing Page down
doDownload = False
searchPos = [1031, 210]
downloadPos = [817, 396]
closePos = [968, 486]
anotherPos = [1088, 391]
outsidePos = [1564, 565]

skipTo = 20 # False

yPosDiff = yPosition2 - yPosition
exceeded = False


def trackmouse():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n') 

# trackmouse()

def verifyMouse():
    if count == maxTrackPerPage +2:
        pyautogui.sleep(1)
    if count == maxTrackPerPage +1:
            pyautogui.sleep(1)
            pyautogui.press('pagedown')
            pyautogui.sleep(3)

    pyautogui.moveTo(x=xPosition, y=yPosition, duration=0.2)
    if count == maxTrackPerPage +1:
        pyautogui.sleep(1)

def checkStatus(text, sleepDuration = 3):
    pyautogui.sleep(sleepDuration)
    while True:
        pyautogui.click(x=outsidePos[0], y=outsidePos[1])
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        clipboard_text = pyperclip.paste()
        # print(clipboard_text)
        if text not in clipboard_text:
            print(count, "Not ready..", text)
            pyautogui.sleep(sleepDuration)
        else: 
            print(count, "Ready", text)
            break  

def download():
    pyautogui.click(x=searchPos[0], y=searchPos[1]) # search bar
    pyautogui.typewrite(playlistLink) # paste link
    pyautogui.press('enter') # enter
    checkStatus(firstSongName, 1)
    
    if exceeded + 1:
        pyautogui.sleep(1)
    if exceeded:
        pyautogui.sleep(1)
        pyautogui.press('pagedown') # move to next track
        pyautogui.sleep(2)

    pyautogui.moveTo(x=xPosition, y=yPosition, duration=0.2) # move to next track
    pyautogui.click() # download button
    pyautogui.sleep(2)

    if exceeded:
        pyautogui.press('home')

    # Enable one:
    # pyautogui.sleep(30)
    checkStatus("Download MP3", 2)
    
    pyautogui.click(x=downloadPos[0], y=downloadPos[1]) # download track
    pyautogui.sleep(3)

    # Name
    pyautogui.press('left')
    pyautogui.hotkey('ctrl', 'delete')
    pyautogui.hotkey('ctrl', 'delete')
    pyautogui.press('enter') # save

    # Resetting to homepage
    pyautogui.sleep(1)
    pyautogui.click(x=closePos[0], y=closePos[1]) # close
    pyautogui.sleep(1)
    pyautogui.click(x=anotherPos[0], y=anotherPos[1]) # another song
    pyautogui.sleep(5)
    # Now at homepage


pyautogui.click(x=1000, y=1062) # open chrome
pyautogui.sleep(1)


while count <= totalCount:

    # break

    # download()
    verifyMouse()

    # break


    yPosition += yPosDiff
    print(count)
    count += 1

    if count == maxTrackPerPage + 1:
        yPosition = newYPos
    if count >= maxTrackPerPage + 1 and not exceeded:
        exceeded = True
