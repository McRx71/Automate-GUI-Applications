from AutoSR import *
class menu:

    def __init__(self, choice):
       self.choice = choice

    def selectScreen(self):
        print('1) Start script')
        print('2) Close')
        print('3) Statistics')
        self.choice = input('Select: 1 or 2: ')
        if self.choice == '1':
            self.choice = True
        elif self.choice == '2':
            self.choice = False
        print(self.choice)



    def selectScreenLogic(self):
        if self.choice == True:
            while self.choice == True:
                input_champ = input('select your champion: 1')
                input_role = input('select your role[Not working yet]: ')
                action = actions(input_champ, input_role)
                action.fetch()
                action.select()
                Main()
        elif self.selectScreen() == False:
            exit()




def Main():
    m = menu(0)
    m.selectScreen()
    m.selectScreenLogic()

Main()