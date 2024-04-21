#import pyautogui as ag # old: pydirectinput
import pydirectinput as ag
import pygetwindow as gw
import psutil
import keyboard
from time import sleep
from pywinauto import Desktop
import pywin32_system32

process_name = 'BrazosTweaker.exe'
process_path = ''
window_title = 'BrazosTweaker'

def check_processes(process_name):
    verbose_logging = True
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                if process.status() == psutil.STATUS_RUNNING:
                    #isReady = True
                    print('Processo em execução')
                    break

                if verbose_logging:
                    # so funciona se a janela estiver na taskbar
                    win = [w for w in ag.getAllWindows() if window_title in w.title]
                    
                    
                    if len(win)>0:
                        #window = ag.getWindowsWithTitle('Voicemod')[0]
                        if win[0].isMinimized:
                            win[0].restore()
                        #ag.getWindowsWithTitle('Voicemod')[0].activate()
                        win[0].activate()
                        win[0].restore()
                        return ('ranela detectada!')
                    #window.activate()
                return 'processo: '+ process.name()

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return 'Looks like it\'s not working.' #print("Looks like it's not working.")
            pass


d = 0.75

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# position_matrix = (Position(30,143), # tab
#                  Position(167,170), # value

#                  Position(77, 145),
#                  Position(166,164),

#                  Position(122,144),
#                  Position(170,163),

#                  Position(323,300))

position_matrix = [
    [30, 143],  # posição para 'tab'
    [167, 170], # posição para 'value'
    [77, 145],
    [166, 164],
    [122, 144],
    [170, 163],
    [323, 300]  # posição final, possivelmente para 'apply' ou 'confirm'
]

# for pos in position_matrix:
#     print(f'{pos.x}, {pos.y}')
print(position_matrix)
print(f'---- done')
values_list = ['1,75', '3,25', '5,00']

def move_mouse(x,y):
    ag.moveTo(x,y,d)

# tete de movimentacao do mouuse

for pos in position_matrix:
    move_mouse(pos)

# for row in position_matrix:
#     for col in row:
#         # Concatenate the current element to the string
#         string_matrix += col


def set_value(val):
    if val != None:
        try:
            # for c in val:
            #     if c == ".":
            #         val = val.replace(c,",")
            stripped = [c.strip() for c in val.split(',')]
            print(f'stripped :1{stripped}')
            ag.write('f{stripped[0]},{stripped[2]}')
            
            print(f'stripped string val: '+
                  '{stripped[0]}{stripped[1]}{stripped[2]}')
        except:
            pass
        

##################################

#sg.theme('Reddit')

def move_window_to_zero():
    window = gw.getWindowsWithTitle(window_title + ' V1.0.7')[0]
    print(f'processo encontrado: {window.title}')
    window.activate()
    sleep(0.35)
    window.moveTo(0,0)
    sleep(0.25)
    

def overclock():
    move_window_to_zero()
    for idx, position in enumerate(position_matrix):
        move_mouse(position[0], position[1])  # Acessa x como position[0] e y como position[1]
        value = None
        if idx < len(values_list):
            value = values_list[idx]
        print(f'idx {idx}, position {position}, value {value}')
        if value:
            ag.doubleClick()
            sleep(0.15)
            ag.write(value)
        else:
            print('Value does not exist f')


print('Primeiro tenha a janela do BrazosTweaker aberta.\n Agora, pressione alguma tecla:\n'+
      '1 - Fazer overclock\n'+
      '2 - Sair')

firstTimeDone = False

def automate():
    move_mouse(14,30)
    ag.click()
    sleep(0.15)
    overclock()
    sleep(0.15)
    global firstTimeDone
    if firstTimeDone == False:
        firstTimeDone = True

option = input('>')
if option == '1':
    automate()
else:
    exit()

while firstTimeDone:

    if keyboard.is_pressed('escape'):
        exit()
        break
    opc = input('Continuar?\n1 - sim\n2 - Não\n>')
    if opc == '1': automate()
    else: exit()
#     current_status = check_processes(process_name)
#     if current_status != None:
#         print('status: '+ check_processes(process_name))
#     print('esc para sair')




    










