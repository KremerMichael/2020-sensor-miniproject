#!/usr/bin/env python3
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math

def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    rooms = ["office", "lab1", "class1"]
    measurements = ["temperature", "occupancy", "co2"]

    #Printing median and variance observed from temp and occupancy data
    print("Median and Variance:")
    for measurement in measurements:
        df = data[measurement]
        for room in rooms:
            stack = df[room]
            stack_data = stack.dropna() 
            median = statistics.median(stack_data)
            variance = statistics.variance(stack_data)
            if measurement != "co2":
                print("The Median " + str(room) + " " + str(measurement) + " is " + str(median))
                print("The Variance of " + str(measurement) + " in " + str(room) + " is " + str(variance))
    print("\n")
              
    #plot probability dist function for each sensor
    print("Printing Probability Distributions:")
    for measurement in measurements:
        df = pandas.DataFrame(data[measurement])
        Title="Probability Distribution Function of " + str(measurement)
        df.plot.kde(title=Title)
    print("\n")

    #Mean, variance, and pdf of time interval data
    print("Time-Interval Mean and Variance:")
    for measurement in measurements:
        df = data[measurement]
        time_dict = {}
        for room in rooms:
            stack = df[room]
            stack_data = stack.dropna()
            time_diff = [0] * (stack_data.size - 1)
            for x in range (0, stack_data.size):
                if x != 0:
                    time_diff[x - 1] = float(stack_data.index[x].timestamp() - stack_data.index[x - 1].timestamp())
            time_dict[room] = time_diff
            mean = statistics.mean(time_diff)
            variance = statistics.variance(time_diff)
            print("The Mean Time Difference of " + str(measurement) + " Measurements in " + str(room) + " is " + str(mean))
            print("The Variance of Time Difference in " + str(measurement) + " Measurements in " + str(room) + " is " + str(variance))
        pd_dict = dict( office = np.array(time_dict["office"]), lab1 = np.array(time_dict["lab1"]), class1 = np.array(time_dict["class1"]))
        df2 = pandas.DataFrame(dict([ (k,pandas.Series(v)) for k, v in pd_dict.items() ]))
        Title="Probability Distribution Function of Time Difference in " + str(measurement) + " Measurements"
        df2.plot.kde(title=Title)
            
    plt.show()
