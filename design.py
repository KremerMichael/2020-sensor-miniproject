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
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r - json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])
            temerature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {"temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
            "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
            "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),}

    return data

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyze IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()
    data = load_data(file)
