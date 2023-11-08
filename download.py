import pyautogui

# https://spotifydown.com/
# zoom out to 50%

count = 1
scroll = 0

playlistLink = "https://open.spotify.com/playlist/06BMp2O4VZ3QgTw6V294oc"
totalCount = 32
maxTrackPerPage = 16
xPosition = 1183 #starting track x position
yPosition = 395 #starting track y position
yPosition2 = 435 #2nd track y position
newYPos = 238 # after pressing Page down
doDownload = False
searchPos = [1031, 210]
closePos = [968, 486]
anotherPos = [1088, 391]

yPosDiff = yPosition2 - yPosition
exceeded = False

def verifyMouse():
    
    if count == maxTrackPerPage +2:
        pyautogui.sleep(1)
    if count == maxTrackPerPage +1:
            pyautogui.sleep(1)
            pyautogui.press('pagedown')
            pyautogui.sleep(2)

    pyautogui.moveTo(x=xPosition, y=yPosition, duration=0.2)
    if count == maxTrackPerPage +1:
        pyautogui.sleep(1)


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

def download(scrollCount):
    pyautogui.click(x=searchPos[0], y=searchPos[1]) # search bar
    pyautogui.typewrite(playlistLink) # paste link
    pyautogui.press('enter') # enter
    pyautogui.sleep(5)

    if count == maxTrackPerPage +1:
        pyautogui.sleep(1)
        pyautogui.press('pagedown')
        pyautogui.sleep(2)

    pyautogui.moveTo(x=xPosition, y=yPosition, duration=0.2)
    # pyautogui.click() # download button
    pyautogui.sleep(1)
    # if scrollCount > 0:
    #     pyautogui.press('home')
    # pyautogui.sleep(30)
    # pyautogui.click(x=842, y=303) # download track
    # pyautogui.sleep(3)

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

    # Download:
    # download()
    # if exceeded + 1:
    #     pyautogui.sleep(1)
    # if exceeded:
    #         pyautogui.sleep(1)
    #         pyautogui.press('pagedown')
    #         pyautogui.sleep(2)
    # pyautogui.moveTo(x=xPosition, y=yPosition, duration=0.2)
    # pyautogui.click()
    # if count == maxTrackPerPage + 1:
    #     pyautogui.sleep(1)

    verifyMouse()

    yPosition += yPosDiff
    print(count)
    count += 1
    if count == maxTrackPerPage + 1:
        yPosition = newYPos
    if count >= maxTrackPerPage + 1:
        exceeded = True


    # break
    # verifyMouse()
    # yPosition += yPosDiff
    # if yPosition > 1030:
    #     # if scroll == 1:
    #     #     # 2 scroll
    #     #     yPosition = 200

    #     # 1 scroll
    #     yPosition = 238
    #     scroll += 1

    # print(count)
    # count += 1
