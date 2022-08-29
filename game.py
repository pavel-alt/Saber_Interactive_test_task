import os
from functools import cached_property
from time import sleep

import pyautogui as pag


class Game:
    def __init__(self, path_to_game):
        self.path_to_game = path_to_game

    @cached_property
    def centre_point(self):
        """
        - gives a pixel on the screen, the color of which will change after the game is loaded
        :return: Tuple[int, int], coordinates
        """
        size = pag.size()
        centre_point = (size[0] // 2, size[1] // 3)
        return centre_point

    @staticmethod
    def __push_key(key, hold=0.1, number=1):
        """
        - pressing a button
        :param key: str, button's name
        :param hold: float, time keyDown's work
        :param number: int, number of clicks
        :return: None
        """
        for _ in range(number):
            pag.keyDown(key)
            sleep(hold)
            pag.keyUp(key)
            sleep(hold)

    def __wait(self):
        """
        - skip splash screen
        :return: None
        """
        sleep(5)
        x, y = self.centre_point
        pag.moveTo(x, y)
        start_color = pag.pixel(x, y)
        while pag.pixel(x, y) == start_color:
            sleep(1)

    def load(self):
        """
        - launch exe file
        :return: None
        """
        os.system(self.path_to_game)

    def start_new_game(self):
        """
        - click "start game" after skipping the splash screen
        :return: None
        """
        self.__wait()
        self.__push_key('enter', number=2)

    def run(self, duration):
        """
        - character moving forward
        :param duration: int, the time of moving
        :return: None
        """
        self.__push_key('w', hold=duration)

    def get_stat(self):
        """
        - start fps monitor by hotkey
        :return: None
        """
        self.__push_key('8')

    def game_over(self):
        """
        - press key combination to exit the game
        :return: None
        """
        self.__push_key('esc')
        self.__push_key('down', number=2)
        self.__push_key('enter')
        self.__push_key('down', number=2)
        self.__push_key('enter')
