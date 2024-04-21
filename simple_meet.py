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
    # Mover a janela para a posição (0,0)
    move_window_to_zero()

    profile = 1 # (balance=1)
    # open dropdown and click
    move_mouse(36,298)
    ag.click()

    if profile == 1: #balance
        move_mouse(36,316)
        ag.click()
    elif profile == 2: #ultra
        move_mouse(36,331)
        ag.click()
    elif profile == 3: #max
        move_mouse(36,343)
        ag.click()


    # Percorrendo todas as posições em position_list
    for idx, position in enumerate(position_list):
        # Mover o mouse para cada posição em position_list
        ag.moveTo(position.x, position.y, 0.75)
        
        print(f'Movendo o mouse para a posição ({position.x}, {position.y})')
        
        # Verificar se idx é ímpar para atribuir valores de values_list
        if idx % 2 == 1:
            if idx // 2 < len(values_list):
                value = values_list[idx // 2]
                ag.doubleClick()
                sleep(0.15)
                print(f'idx {idx}, position ({position.x}, {position.y}), value {value}')
                ag.write(value)
            else:
                print(f'Sem valor correspondente em values_list para idx {idx}.')
        elif position.x == 323 and position.y == 300:
            ag.click()
            print('\nOverclock aplicado!!')
        else:
            ag.click()


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