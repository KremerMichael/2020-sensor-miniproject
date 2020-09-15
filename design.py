#!/usr/bin/env python3
#

import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import numpy as np
import statistics

def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:
    temperature = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])
            temperature[time] = {room: r[room]["temperature"][0]}

    data = {"temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),}
    return data

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyze IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    #Get data
    data = load_data(file)

    rooms = ["office", "lab1", "class1"]

    stdev_mod = 1

    for room in rooms:
        print("searching for temperature anomalies in " + room)
        room_temps = data["temperature"][room].dropna()
        room_mean = statistics.mean(room_temps)
        room_stdev = statistics.mean(room_temps)
        for x in range(0, room_temps.size):
            temp = room_temps.iloc[x]
            deviation = abs(temp - room_mean)
            bound = room_stdev * stdev_mod
            if deviation > bound:
                print("Anomaly detected!")
                print("At " + str(room_temps.index[x]) + " the temperature was " + str(room_temps[x]))
        print("\n")

    #Store temperatures by room
    #office_temp = data["temperature"]["office"].dropna()
    #lab1_temp = data["temperature"]["lab1"].dropna()
    #class1_temp = data["temperature"]["class1"].dropna()

    #Get mean
    #office_mean = statistics.mean(office_temp)
    #lab1_mean = statistics.mean(lab1_temp)
    #class1_mean = statistics.mean(class1_temp)

    #Get std deviation
    #office_stdev = statistics.stdev(office_temp)
    #lab1_stdev = statistics.stdev(lab1_temp)
    #class1_stdev = statistics.stdev(class1_temp)

    #stdev_mod = 1
    #print(lab1_mean)
    #print(lab1_stdev)
    #for x in range(0, lab1_temp.size):
    #temp = lab1_temp.iloc[x]
     #   if abs(temp - lab1_mean) > (lab1_stdev * stdev_mod):
      #      print(temp)


    #print(data)
    #print(office_temp)
    #print(lab1_temp)
    #print(class1_temp)
