import pyautogui, os, time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def clickImage(imagepath):
    buttonBox = (None, None, None, None)
    while not all(buttonBox):
        print(buttonBox, imagepath)
        buttonBox = pyautogui.locateOnScreen(imagepath, grayscale=True)
        if buttonBox == None:
            buttonBox = (None, None, None, None)
    print(buttonBox)
    buttonpoint = pyautogui.center(buttonBox)
    pyautogui.mouseDown(buttonpoint, button='left');
    pyautogui.mouseUp(buttonpoint, button='left')
    print(buttonpoint)

def selectChamp():
    clickImage('random.bmp')
    clickImage('lockin.bmp')

    
selectChamp()



