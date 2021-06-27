from AutoSR import *
from statistics import *
from TFT.AutoTFT import *
class menu:

<<<<<<< Updated upstream
	def __init__(self):
		print('1) Start script')
		print('2) Statistics')
		print('3) AutoTFT')
		print('4) Close')

	def selectScreen(self):
		menu_opt = input('Select: ')
		self.choice = True
		if menu_opt == '1':
			self.action = 'AutoSR'
		elif menu_opt == '2':
			self.action = 'statistics'
		print(self.choice)
		if menu_opt == '3':
			self.action = 'tft'
		print(self.choice)
		if menu_opt == '4':
			self.choice = False
			self.action = 'close'
		print(self.choice)



	def selectScreenLogic(self):
		if self.choice == True:
			while self.choice == True:
				if self.action == 'AutoSR':
					input_champ = input('select your champion: ')
					input_role = input('select your role[Not working yet]: ')
					action = actions(input_champ, input_role)
					action.fetch()
					action.select()
					Main()
				elif self.action == 'statistics':
					pass
				elif self.action == 'tft':
					tft_main()
				else:
					exit()


		elif self.selectScreen() == 'close':
			exit()
=======
    def __init__(self, choice, action):
       self.choice = choice
       self.action = action

    def selectScreen(self):
        print('1) Start script')
        print('2) Statistics')
        print('3) Close')

        menu_opt = input('Select: ')
        self.choice = True
        if menu_opt == '1':
            self.action = 'AutoSR'
        elif menu_opt == '2':
            self.action = 'statistics'
        print(self.choice)
        if menu_opt == '3':
            self.choice = False
            self.action = 'close'
        print(self.choice)



    def selectScreenLogic(self):
        if self.choice == True:
            while self.choice == True:
                if self.action == 'AutoSR':
                    input_champ = input('select your champion: 1')
                    input_role = input('select your role[Not working yet]: ')
                    action = actions(input_champ, input_role)
                    action.fetch()
                    action.select()
                    Main()
                elif self.action == 'statistics':
                    pass

        elif self.selectScreen() == 'close':
            exit()
>>>>>>> Stashed changes




def Main():
	m = menu()
	m.selectScreen()
	m.selectScreenLogic()

Main()