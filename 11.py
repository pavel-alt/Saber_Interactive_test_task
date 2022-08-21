import os
from multiprocessing import Process
from time import sleep

import keyboard
import pyautogui as pag
from pygetwindow import getWindowsWithTitle, getAllTitles


def func2():
    os.system("C:/Users/Katerina/Desktop/pno0001.exe")


def func1():
    print("Функция У ожидает")
    sleep(45)
    print("Функция У в работе")

    pag.keyDown('esc')
    sleep(0.1)
    pag.keyUp('esc')
    sleep(2)
    pag.keyDown('enter')
    sleep(0.1)
    pag.keyUp('enter')


if __name__ == '__main__':
     p1 = Process(target=func1)
     p1.start()
     p2 = Process(target=func2)
     p2.start()

