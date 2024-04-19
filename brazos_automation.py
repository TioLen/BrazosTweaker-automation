import pyautogui as ag
import pygetwindow as gw
import psutil
import PySimpleGUI as sg
from time import sleep


process_name = ''
process_path = ''
window_title = ''

program = 'brazos'


if program == 'brazos':
    window_title = 'BrazosTweaker'
    process_name = 'BrazosTweaker.exe'
    process_path = f'C:\Program Files\BrazosTweaker\{process_name}'
else:
    window_title = 'Voicemod'
    process_name = 'VoicemodDesktop.exe'
    process_path = f'C:\Program Files\Voicemod Desktop\{process_name}'


appWindow = None
isReady = False

def run_process():
    ag.hotkey('win', 'r')
    ag.write(process_path)
    ag.press('enter')
    for i in range(5, 0, 1):
        sleep(i)
        print(f'Buscando aplicação... tentativas restantes: {i}')

process_window = None
win_geometries = [0,0,0,0]

def set_window_ref(window):
    process_window = window

def set_win_geometries(x,y,w,h):
    win_geometries[0] = x
    win_geometries[1] = y
    win_geometries[2] = w
    win_geometries[3] = h

def check_processes(process_name):
    verbose_logging = True
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                if process.status() == psutil.STATUS_RUNNING:
                    #isReady = True
                    print('Processo em execução')
                    break
                else:
                    run_process()

                if verbose_logging:
                    # so funciona se a janela estiver na taskbar
                    win = [w for w in ag.getAllWindows() if window_title in w.title]
                    
                    
                    if len(win)>0:
                        #window = ag.getWindowsWithTitle('Voicemod')[0]
                        if win[0].isMinimized:
                            win[0].restore()
                        #ag.getWindowsWithTitle('Voicemod')[0].activate()
                        win[0].activate()
                        x = win_geometries[0]
                        y = win_geometries[1]
                        w = win_geometries[2]
                        h = win_geometries[3]
                        set_win_geometries(x,y,w,h)
                        print('geos: '+win_geometries)
                        isReady = True
                        return ('ranela detectada!')
                    #window.activate()
                return 'processo: '+ process.name()
            else:
                if process.status() != psutil.STATUS_RUNNING:
                    run_process()
                print(f'----- process: {process.name()}')

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

values_list = [1.75, 3.25, 5]

def move_mouse(x,y):
    ag.moveTo(x,y,d)
              
##################################

sg.theme('Reddit')

program_states = ['Inicializando programa...', 'Maximizando janela...', 'Pronto para otimização.', 'Overclock realizado!']


layout = [[sg.Text(program_states[0])],
          [sg.Text('debug', key='status')],
          [sg.Button('abroba')],
          [sg.Button('Otimizar')]]

window = sg.Window('Brazos Automation', layout, finalize=True)

#window.read()

gap = 8
while True:
    try:
        print('exists? --> '+ process_window)
    except:
        pass
    if process_window != None and process_window != process_window.isMinimized:
        geometry = ag.getWindowGeometry(process_window)
        print(f'> pos X: {geometry[0]}, pos Y: {geometry[1]}')
        print(f'> width: {geometry[2]}, height: {geometry[3]}\n')
        ag.moveTo((gap + geometry[0] + geometry[2]),(geometry[1] + geometry[3]))


    current_status = check_processes(process_name)
    if current_status != None:
        print('status: '+ check_processes(process_name))

    if not isReady:
        events, values = window.read()
        
        if events == sg.WINDOW_CLOSED:
            break

        found = window['status'].update(check_processes(process_name))

        if found:
            if appWindow != None: appWindow.activate()
        if events == 'Otimizar' and isReady == True:

            #click on icon
            #ag.moveTo(170,750,0.15)
            #ag.click(interval=0.1)
            #sleep(0.3)
            
            for position in position_list:
                move_mouse(position.x, position.y)
            if position.x == 323 and position.y == 300:
                print('click')



    










