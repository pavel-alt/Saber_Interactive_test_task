import os
from datetime import datetime
from multiprocessing import Process
from time import sleep
import pyautogui as pag

# pag.pixelMatchesColor()

path = "C:/Users/Katerina/PycharmProjects/Saber_Interactive_test_task/Saber_Interactive_test_task"
path_to_run_file = "C:/Users/Katerina/Desktop/pno0001.exe"


def push_the_button(button_name, hold=0.1):
    pag.keyDown(button_name)
    sleep(hold)
    pag.keyUp(button_name)
    sleep(hold)


def run_game():
    os.system(path_to_run_file)


def wait():
    sleep(5)
    # size = pag.size()
    pag.moveTo(600, 500)
    start_color = pag.pixel(600, 500)
    print(f'start_color - {start_color}')
    while pag.pixel(600, 500) == start_color:
        print(f'actual_color - {pag.pixel(600, 500)}')
        sleep(1)
    print('end')


def actions():
    # print("Функция ожидания работает")
    # sleep(45)
    #
    # print("Функция ожидания дождалась")

    wait()
    push_the_button('esc')
    sleep(2)
    push_the_button('enter')

    print(pag.size())

    push_the_button('8')

    sleep(1)
    pag.screenshot(f"{path}/{datetime.now().strftime('%H-%M-%S')}.jpg")
    sleep(1)
    push_the_button('w', 5)

    pag.screenshot(f"{path}/{datetime.now().strftime('%H-%M-%S')}.jpg")

    push_the_button('8')

    push_the_button('esc')

    push_the_button('down')

    push_the_button('down')

    push_the_button('enter')

    push_the_button('down')

    push_the_button('down')

    push_the_button('enter')


if __name__ == '__main__':
    # run_game()
    # wait()
    # actions()
    p1 = Process(target=run_game)
    p1.start()
    # pw = Process(target=wait)
    # pw.start()
    p2 = Process(target=actions)
    p2.start()
