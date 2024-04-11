import pyautogui as ag
import psutil
from time import sleep


process_name = 'BrazosTweaker.exe'
# lang = 'PT-BR', 'EN-US'

# check if the process name matches
# this def uses some logic and boilerplates  
def check_processes(process_name):
    verbose_logging = True
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                if verbose_logging == True:
                    print(f'found: {process.name()}')
                    #window = ag.getWindowsWithTitle(process.name())[0]
                    win = [w for w in ag.getAllWindows() if 'BrazosTweaker' in w.title]
                    if len(win)>0:
                        #win[0].activate()
                        print('letwindherson nunes')
                    #window.activate()
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("Looks like it's not working.")
            pass
    

d = 0.25

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

position_list = (Position(30,143),
                 Position(167,170),

                 Position(77, 145),
                 Position(166,164),

                 Position(122,144),
                 Position(170,163),

                 Position(323,300))

values_list = [1.75, 3.25, 5]
#check_processes(process_name)

# while(True):
#     active_window = ag.hotkey("alt", "tab", interval=0.1)
#     #this win variable stores a list of strings
#     #win = [w for w in ag.getAllWindows() if 'BrazosTweaker' in w.title]

#     if(active_window == str(ag.getWindowsWithTitle('BrazosTweaker'))):
#         break
#open
ag.moveTo(170,750,0.15)
ag.click(interval=0.1)

#admin yes
sleep(1.7)
# ag.moveTo(580,515,0.15)
# ag.click(interval=0.1)
ag.hotkey("left", "enter", interval=0.15)
sleep(0.3)
def move_mouse(x,y):
    ag.moveTo(x,y,d)



for position in position_list:
    move_mouse(position.x, position.y)
    if position.x == 323 and position.y == 300:
        print('click')



