import os
from datetime import datetime
from multiprocessing import Process
from time import sleep
import pyautogui as pag


path = "C:/Users/Katerina/PycharmProjects/Saber_Interactive_test_task/Saber_Interactive_test_task"


def push_the_button(button_name, hold=0.1):
    pag.keyDown(button_name)
    sleep(hold)
    pag.keyUp(button_name)
    # sleep(hold)


def run_game():
    os.system("C:/Users/Katerina/Desktop/pno0001.exe")


def actions():
    print("Функция У ожидает")
    sleep(40)
    print("Функция У в работе")

    push_the_button('esc')
    # sleep(2)
    push_the_button('enter')

    push_the_button('8')

    sleep(1)
    pag.screenshot(f"{path}/{datetime.now().strftime('%H-%M-%S')}.jpg")

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
    p1 = Process(target=actions)
    p1.start()
    p2 = Process(target=run_game)
    p2.start()


