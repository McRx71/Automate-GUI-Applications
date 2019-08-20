import pyautogui, os, time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def clickImage(imagepath):
    buttonBox = (None, None, None, None)
    while not all(buttonBox):
        print(buttonBox, imagepath)
        buttonBox = pyautogui.locateOnScreen(imagepath,grayscale=True)
        if buttonBox == None:
            buttonBox = (None, None, None, None)
    print(buttonBox)
    buttonpoint = pyautogui.center(buttonBox)
    pyautogui.mouseDown(buttonpoint,button='left'); pyautogui.mouseUp(buttonpoint,button='left') 
    print(buttonpoint)

while True:
    clickImage(str('findmatchButton.bmp'))
    clickImage(str('acceptButton.bmp'))
    time.sleep(180)
    pyautogui.mouseDown(buttonpoint,button='left'); pyautogui.mouseUp(buttonpoint,button='left') 
    clickImage(str('openMenuButton.bmp'))
    pyautogui.mouseDown(buttonpoint,button='left'); pyautogui.mouseUp(buttonpoint,button='left') 
    clickImage(str('surrenderButton.bmp'))
    clickImage(str('surrenderCheckButton.bmp'))
    time.sleep(2)
    pyautogui.mouseDown(buttonpoint,button='left'); pyautogui.mouseUp(buttonpoint,button='left') 
    clickImage(str('playagainButton.bmp'))
    pyautogui.moveRel(200, 80)



