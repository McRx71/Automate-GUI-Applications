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
    return buttonpoint


def main():
    while True:
        buttonpoint = clickImage(str('findmatchButton.bmp'))
        clickImage(str('acceptButton.bmp'))
        for x in range(2):
            print('koop')
            buttonBox = pyautogui.locateOnScreen('acceptButton.bmp', grayscale=True)
            if buttonBox != None:
                clickImage(str('acceptButton.bmp'))
                break
        time.sleep(120)
        pyautogui.mouseDown(buttonpoint,button='left'); pyautogui.mouseUp(buttonpoint,button='left')
        buttonpoint = clickImage(str('openMenuButton.bmp'))
        pyautogui.mouseDown(buttonpoint,button='left'); pyautogui.mouseUp(buttonpoint,button='left')
        buttonpoint = clickImage(str('surrenderButton.bmp'))
        buttonpoint = clickImage(str('surrenderCheckButton.bmp'))
        time.sleep(2)
        pyautogui.mouseDown(buttonpoint,button='left'); pyautogui.mouseUp(buttonpoint,button='left')
        buttonpoint = clickImage(str('playagainButton.bmp'))
        pyautogui.moveRel(200, 80)


main()