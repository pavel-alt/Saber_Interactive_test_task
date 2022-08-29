import csv
import os
import shutil
from datetime import datetime
from time import sleep

import pyautogui as pag


class Stat:
    def __init__(self, path_to_stat):
        self.path_to_stat = path_to_stat

    def get_stat_file(self):
        """
        - specifies the path to the location of the newly copied file
        :return: str, path
        """
        x = shutil.copy(f'{self.path_to_stat}/FPSMonitor-benchmark.csv', f'{self.path_to_stat}/FPS_Average.csv')
        return x

    def make_screenshot(self):
        """
        - makes a screenshot-file with the specified name and path
        :return: None
        """
        pag.screenshot(f"{self.path_to_stat}/{datetime.now().strftime('%H-%M-%S')}.jpg")

    def make_average_fps(self):
        """
        - creating a copy of the data file, writing the average fps
        :return: None
        """
        while not os.path.exists(f'{self.path_to_stat}/FPSMonitor-benchmark.csv'):
            sleep(10)
        file = self.get_stat_file()
        with open(file, 'r+') as f:
            reader = csv.DictReader(f)
            all_fps = [int(row['FPS']) for row in reader]
            average = sum(all_fps)/len(all_fps)
            f.seek(0)
            f.truncate()
            f.write(f'FPS Average: {average}')
