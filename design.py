#!/usr/bin/env python3
#

import pandas
from pathlib import Path
import argparse
import json
from datatime import datetime
import typing as T
import numpy as np
import statistics

def load_data(file: path) -> T.Dict[str, pandas.Dataframe]:
    temperature = {}

    with open(file, "r") as f:
        for line in f:
            r - json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])
            temerature[time] = {room: r[room]["temperature"][0]}

    data = {"temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),}
    return data

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyze IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    office_temp = data["temperature"]["office"].dropna()
    lab1_temp = data["temperature"]["lab1"].dropna()
    class1_temp = data["temperature"]["class1"].dropna()

    #Get mean
    office_mean = statistics.mean(office_temp)
    lab1_mean = statistics.mean(lab1_temp)
    class1_mean = statistics.mean(class1_temp)
