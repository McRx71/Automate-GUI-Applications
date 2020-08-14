import pyautogui, os,sys , time, requests
from PIL import Image

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def clickImage(imagepath):
    time.sleep(0.1)
    buttonBox = (None, None, None, None)
    while not all(buttonBox):
        print(buttonBox, imagepath)
        buttonBox = pyautogui.locateOnScreen(imagepath, grayscale=False, confidence=0.6)
        if buttonBox == None:
            buttonBox = (None, None, None, None)
    print(buttonBox)
    buttonpoint = pyautogui.center(buttonBox)
    pyautogui.click(buttonpoint, button='left')

    print(buttonpoint)

def searchChamp(Champion):
    buttonBox = (None, None, None, None)
    while not all(buttonBox):
        print(buttonBox)
        buttonBox = pyautogui.locateOnScreen('searchbar.bmp', grayscale=True)
        if buttonBox == None:
            buttonBox = (None, None, None, None)
    pyautogui.click(buttonBox)
    pyautogui.typewrite(Champion)

def selectRoleBP(role):
    buttonBox = (None, None, None, None)
    while not all(buttonBox):
        print(buttonBox)
        buttonBox = pyautogui.locateOnScreen('chat.jpg', grayscale=True)
        if buttonBox == None:
            buttonBox = (None, None, None, None)
        pyautogui.click(buttonBox)
        pyautogui.typewrite(role)
        pyautogui.press('enter')

def dlSquareAssets(Champion):
    Champion = Champion.capitalize()
    url = 'http://ddragon.leagueoflegends.com/cdn/10.16.1/img/champion/' + Champion + '.png'
    r = requests.get(url, allow_redirects=True)
    open(Champion + '.png', 'wb').write(r.content)

def resizeAssets(Asset, Champion):
    imageFile = Asset
    im1 = Image.open(imageFile)
    width = 64
    height = 64
    im2 = im1.resize((width, height), Image.NEAREST)
    ext = '.jpg'
    im2.save(Champion + ext)

def clean(Champion):
    if os.path.exists(Champion + '.jpg') or os.path.exists(Champion + '.png') :
        os.remove(Champion + '.jpg')
        os.remove(Champion + '.png')
    else:
        print("The file does not exist")

def selectChamp():
    Champion = input()
    dlSquareAssets(Champion)
    resizeAssets(Champion + '.png', Champion)
    searchChamp(Champion)
    clickImage(Champion + '.jpg')
    clean(Champion)
    #selectRoleBP('top')

    #clickImage('random.bmp')
    #clickImage('lockin.bmp')


selectChamp()





