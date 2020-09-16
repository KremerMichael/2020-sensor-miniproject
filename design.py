#!/usr/bin/env python3
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import numpy as np
import statistics

#Function to return pandas DataFrame "Temperature" from JSON txt file
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

#Main
if __name__ == "__main__":
    #Add args and parse
    p = argparse.ArgumentParser(description="load and analyze IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    #Get JSON File from parsed args
    file = Path(P.file).expanduser()

    #Get pandas DataFrame from JSON File
    data = load_data(file)

    #Define Rooms
    rooms = ["office", "lab1", "class1"]

    #This modifier changes how in/out of bounds a temperature data point should be
    #to be considered an anomaly. (Multiples of standard deviation)
    stdev_mod = 1

    #Iterate through rooms
    for room in rooms:
        print("\nsearching for temperature anomalies in " + room + "\n")
        #Drop NaN values
        room_temps = data["temperature"][room].dropna()
        #Get Mean and std deviation
        room_mean = statistics.mean(room_temps)
        room_stdev = statistics.stdev(room_temps)
        #Set bound on temperature
        bound = room_stdev * stdev_mod
        #For keeping track of anomalies
        anomalies = 0
        bad_index = []

        #Iterate over temperature values
        for x in range(0, room_temps.size):
            #Get temp value and deviation from mean
            temp = room_temps.iloc[x]
            deviation = abs(temp - room_mean)
            #Anomaly detected
            if deviation > bound:
                print("Anomaly detected!")
                print("At " + str(room_temps.index[x]) + " the temperature was " + str(round(room_temps[x], 2)))
                #Keeping list of anomaliy indexes
                anomalies+=1
                bad_index.append(room_temps.index[x])

        #Get percent of anomalies
        percent = anomalies / room_temps.size * 100
        print("\nIn " + room + " " + str(anomalies) + " were detected (" + str(round(percent, 2)) + "%)")
        #Drop anomalies
        clean_temps = room_temps.drop(bad_index)
        #Recalculate median and variance with anomaly free data
        clean_median = statistics.median(clean_temps)
        clean_variance = statistics.variance(clean_temps)
        #Prints for Dayz
        print("After removing anomalies from temperature data in " + room)
        print("The new median temperature is " + str(round(clean_median, 2)))
        print("The new variance of temperature is " + str(round(clean_variance, 2)))
        print("----------------------------------------------------------------------")

