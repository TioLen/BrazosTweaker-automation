import pydirectinput as ag
import pygetwindow as gw
import psutil
import keyboard
from time import sleep

process_name = 'BrazosTweaker.exe'
process_path = ''
window_title = 'BrazosTweaker'

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

position_list = (Position(30,143), #click tab
                 Position(167,170), #click input

                 Position(77, 145),
                 Position(166,164),

                 Position(122,144),
                 Position(170,163),

                 Position(323,300))

def check_processes(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name and process.status() == psutil.STATUS_RUNNING:
                print('Processo em execução')
                break
            win = [w for w in ag.getAllWindows() if window_title in w.title]
            if len(win) > 0:
                if win[0].isMinimized:
                    win[0].restore()
                win[0].activate()
                win[0].restore()
                return 'Janela detectada!'
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# position_list = [
#     [30, 143],  # posição para 'tab'
#     [167, 170], # posição para 'value'
#     [77, 145],
#     [166, 164],
#     [122, 144],
#     [170, 163],
#     [323, 300]  # posição final, possivelmente para 'apply' ou 'confirm'
#]

values_list = ['1,75', '3,25', '5,00']

def move_mouse(x, y):
    ag.moveTo(x, y, 0.75)

def move_window_to_zero():
    window = gw.getWindowsWithTitle(window_title + ' V1.0.7')[0]
    window.activate()
    sleep(0.35)
    window.moveTo(0,0)
    sleep(0.25)

def overclock():
    move_window_to_zero()
    for idx in range(1, len(position_list), 2):
        position = position_list[idx]
        #move_mouse(position[0], position[1])
        move_mouse(position.x, position.y)
        print(f'Movendo o mouse para a posição ({position.x}, {position.y})')

        # Verifica se há um valor correspondente em values_list para o índice atual
        if idx // 2 < len(values_list):
            value = values_list[idx // 2]
            ag.doubleClick()
            sleep(0.15)
            print(f'idx {idx}, position {position}, value {value}')
            ag.write(value)
        else:
            print(f'Sem valor correspondente em values_list para idx {idx}.')

print('Primeiro tenha a janela do BrazosTweaker aberta.\nAgora, pressione alguma tecla:\n1 - Fazer overclock\n2 - Sair')

option = input('>')
if option == '1':
    overclock()
else:
    exit()

while True:
    if keyboard.is_pressed('escape'):
        exit()
    opc = input('Continuar?\n1 - sim\n2 - Não\n>')
    if opc == '1':
        overclock()
    else:
        exit()