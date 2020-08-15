from AutoSR import  *
class menu:

    def __init__(self, opt1, opt2):
        self.opt1 = opt1
        self.opt2 = opt2

    def selectScreen(self):
        print('1) Start script')
        print('2) Close')
        choice = input('Select: 1 or 2: ')
        if choice == '2':
            exit()
        elif choice == '1':
            choice = True
        else:
            choice = False
        if choice == True:
            while choice == True:
                input_champ = input('select your champion: 1')
                input_role = input('select your role[Not working yet]: ')
                action = actions(input_champ, input_role)
                action.fetch()
                action.select()
                choice = input('Select another champ?')
        else:
            exit()







def Main():
    m = menu(None, None)
    m.selectScreen()


Main()