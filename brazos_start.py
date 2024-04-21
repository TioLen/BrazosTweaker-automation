import pydirectinput as ag
import pygetwindow as gw
import keyboard
from time import sleep

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

                 Position(323,300)) # last position

window_title = 'BrazosTweaker'

debug = False

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
        
        if debug: print(f'Movendo o mouse para a posição ({position.x}, {position.y})')
        
        # Verificar se idx é ímpar para atribuir valores de values_list
        if idx % 2 == 1:
            if idx // 2 < len(values_list):
                value = values_list[idx // 2]
                ag.doubleClick()
                sleep(0.15)
                if debug:
                    print(f'idx {idx}, position ({position.x}, {position.y}), value {value}')
                ag.write(value)
            else:
                if debug:
                    print(f'Sem valor correspondente em values_list para idx {idx}.')
        elif position.x == 323 and position.y == 300:
            ag.click()
            print('')
            print('##########################')
            print('#  Overclock aplicado!!  #')
            print('##########################\n')
        else:
            ag.click()

    sleep(1)

    window = gw.getWindowsWithTitle(window_title + ' V1.0.7')[0]
    window.minimize()

    print('Tenha um bom proveito!\n')
    sleep(3)

    print('LinkedIn: https://www.linkedin.com/in/tiolen/')
    sleep(1)
    print('GitHub: https://github.com/tiolen')
    print(3)

    print('\nFechando...')
    sleep(1)
    exit()


#print('Primeiro tenha a janela do BrazosTweaker aberta.\nAgora, pressione alguma tecla:\n1 - Fazer overclock\n2 - Sair')

print(" ##################################################################")
print(" #                                                                #")
print(" #  A janela do BrazosTweaker abriu ou está abrindo,              #")
print(" #  por favor espere abrir primeiro.                              #")
print(" #                                                                #")
print(" ##################################################################")
sleep(1)
print(" -------- Pressione alguma das teclas abaixo e aperte Enter -------")
print(" ------------------------------------------------------------------")
print("")
sleep(0.5)
print(" 1 - Otimizar computador")
print(" 2 - Sair")

option = input(' >')
if option == '1':
    overclock()
else:
    exit()

while True:
    if keyboard.is_pressed('escape'):
        exit()