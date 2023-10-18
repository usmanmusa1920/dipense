# -*- coding: utf-8 -*-
import os
# Using shutil to move recent files into the sec folder
import shutil
from pathlib import Path
from datetime import datetime


today = datetime.today()


def age():
    for i in os.listdir():
        if os.path.isfile(i):
            l = ['db.sqlite3', 'dump.json']
            if os.path.basename(i) not in l:
                mtime = datetime.fromtimestamp(os.stat(i)[8])
                filetime = mtime - today
                if abs(filetime.days) <= 1:
                    # print(mtime,f" {os.path.basename(i)} older {abs(filetime.days)} days")
                    # print(mtime.year, mtime.month, mtime.day, mtime.hour, mtime.minute, mtime.second, 'm')
                    # print(today.year, today.month, today.day, today.hour, today.minute, today.second, 't')
                    # print()

                    directory = os.path.join(
                        Path(__file__).resolve().parent.parent, 'sec')
                    # Create a timestamp
                    timestamp = datetime.now()
                    # We move any .csv files in the folder to the backup folder.
                    # shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)
                    shutil.move(os.path.basename(i), directory + '/' + os.path.basename(i))
