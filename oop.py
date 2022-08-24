import argparse
import os
from datetime import datetime
from functools import cached_property
from multiprocessing import Process
from time import sleep

import pyautogui as pag


class Game:
    def __init__(self, path_to_game, path_to_stat):
        self.path_to_game = path_to_game
        self.path_to_stat = path_to_stat

    @cached_property
    def screen_coord(self):
        
        return


    def start_new_game(self):
        """
        - пропустить заставку ф-ция wait()
        - нажать 'start game'
        :return: None
        """
        pass

    def game_over(self):
        """
        - жать esc пока не выйдет
        :return: None
        """
        pass

    def wait(self):
        sleep(5)
        size = pag.size()
        pag.moveTo(600, 500)
        start_color = pag.pixel(600, 500)
        print(f'start_color - {start_color}')
        while pag.pixel(600, 500) == start_color:
            print(f'actual_color - {pag.pixel(600, 500)}')
            sleep(1)
        print('end')
        """
        - пропуск заставки
        :return: None
        """
        pass

    def make_screenshoot(self):
        pag.screenshot(f"{path}/{datetime.now().strftime('%H-%M-%S')}.jpg")


def argument_parser():
    parser = argparse.ArgumentParser(description="kkrieger's run parser ")
    parser.add_argument("path_to_kkrieger", type=str)
    parser.add_argument('-o', type=str, default=os.getcwd())
    args = parser.parse_args()
    return args


def test_scenario(game):
    game.start_new_game()
    game.make_screenshoot()
    game.get_stat()
    game.run(duration=5)
    game.get_stat()
    game.make_screenshoot()




if __name__ == '__main__':
    args = argument_parser()
    game = Game(args.path_to_kkrieger, args.o)
    game_process = Process(target=game.load)
    game_process.start()
    test_process = Process(target=test_scenario(game))
    test_process.start()
