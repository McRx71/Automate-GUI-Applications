import pyautogui, os,sys , time, requests
from PIL import Image

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class championAssets:
    def __init__(self, champ):
        self.champ = champ

    def dlSquareAssets(self):
        self.champ = self.champ.capitalize()
        url = 'http://ddragon.leagueoflegends.com/cdn/10.16.1/img/champion/' + self.champ + '.png'
        r = requests.get(url, allow_redirects=True)
        open(self.champ + '.png', 'wb').write(r.content)

    def resizeAssets(self):
        imageFile = self.champ + '.png'
        im1 = Image.open(imageFile)
        width = 64
        height = 64
        im2 = im1.resize((width, height), Image.NEAREST)
        ext = '.jpg'
        im2.save(self.champ + ext)

    def clean(self):
        if os.path.exists(self.champ + '.jpg') or os.path.exists(self.champ + '.png'):
            os.remove(self.champ + '.jpg')
            os.remove(self.champ + '.png')
        else:
            print("The file does not exist")

class champSelect:
    def __init__(self, champ, role):
        self.champ = champ
        self.role = role

    def clickImage(self):
        imgpath = self.champ + '.jpg'
        time.sleep(0.1)
        buttonBox = (None, None, None, None)
        while not all(buttonBox):
            print(buttonBox, imgpath)
            buttonBox = pyautogui.locateOnScreen(imgpath, grayscale=False, confidence=0.6)
            if buttonBox == None:
                buttonBox = (None, None, None, None)
        print(buttonBox)
        buttonpoint = pyautogui.center(buttonBox)
        pyautogui.click(buttonpoint, button='left')

        print(buttonpoint)

    def searchChamp(self):
        buttonBox = (None, None, None, None)
        while not all(buttonBox):
            print(buttonBox)
            buttonBox = pyautogui.locateOnScreen('searchbar.bmp', grayscale=True)
            if buttonBox == None:
                buttonBox = (None, None, None, None)
        pyautogui.click(buttonBox)
        pyautogui.typewrite(self.champ)

    def selectRoleBP(self):
        buttonBox = (None, None, None, None)
        while not all(buttonBox):
            print(buttonBox)
            buttonBox = pyautogui.locateOnScreen('chat.jpg', grayscale=True)
            if buttonBox == None:
                buttonBox = (None, None, None, None)
            pyautogui.click(buttonBox)
            pyautogui.typewrite(self.role)
            pyautogui.press('enter')

class actions:
    def __init__(self, input_champ, input_role):
        self.input_champ = input_champ
        self.input_role = input_role



    def fetch(self):
        champ = championAssets(self.input_champ)
        champ.dlSquareAssets()
        champ.resizeAssets()
        #champ.clean()


    def select(self):
        pick = champSelect(self.input_champ,  self.input_role)
        pick.searchChamp()
        pick.clickImage()
        pick.selectRoleBP()

#fetch(input_champ)
#select(input_champ)