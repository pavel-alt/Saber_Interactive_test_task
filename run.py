import argparse
import os

from multiprocessing import Process

from game import Game
from stat_game import Stat
from test_for_kkrieger import test_scenario


def argument_parser():
    parser = argparse.ArgumentParser(description="kkrieger's run parser ")
    parser.add_argument("path_to_kkrieger", type=str)
    parser.add_argument('-o', type=str, default=os.getcwd())
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = argument_parser()
    game = Game(args.path_to_kkrieger)
    stat = Stat(args.o)
    game_process = Process(target=game.load)
    game_process.start()
    test_process = Process(target=test_scenario(game, stat))
    test_process.start()
    game_process.terminate()
    test_process.terminate()
