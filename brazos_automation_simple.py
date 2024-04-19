import pyautogui as ag # old: pydirectinput
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

values_list = ['1,75', '3,25', '5,00']

def move_mouse(x,y):
    ag.moveTo(x,y,d)
              
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

def overclock():
    for idx, position in enumerate(position_list):
        move_mouse(position.x, position.y)
        ag.doubleClick()
        try:
            value = values_list[idx]
            if value != None:
                try:
                    # for c in val:
                    #     if c == ".":
                    #         val = val.replace(c,",")
                    # stripped = [c.strip() for c in value.split(',')]
                    print(f'values_list[idx] {values_list[idx]}')
                    stripped = str(values_list[idx]).split(',')
                    print(f'stripped string val: {stripped[0]}{stripped[1]}{stripped[2]}')
                    ag.write('f{stripped[0]}{stripped[1]}{stripped[2]}')
                    
                except:
                    pass
        except:
            continue
        
        print(f'valores: ({position_list[idx].x}, {position_list[idx].y}) = {value}')
    
    if position.x == 323 and position.y == 300:
        print('click')

program_states = ['Inicializando programa...', 'Maximizando janela...', 'Pronto para otimização.', 'Overclock realizado!']

print('Primeiro tenha a janela do BrazosTweaker aberta.\n Agora, pressione alguma tecla:\n'+
      '1 - Fazer overclock\n'+
      '2 - Sair')

firstTimeDone = False

def automate():
    move_mouse(14,30)
    ag.click()
    sleep(0.15)
    # ag.click()
    # sleep(0.1)
    # ag.click()
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

    opc = input('Continuar?\n1 - sim\n2 - Não\n>')
    if opc == '1': automate()
    else: exit()
#     current_status = check_processes(process_name)
#     if current_status != None:
#         print('status: '+ check_processes(process_name))
#     print('esc para sair')




    










