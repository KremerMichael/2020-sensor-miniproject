Michael Kremer
U45121665
END EC463 A1
# 2020 Sensor Mini-Project Report

## Task 0: Set up Python Websockets
The greeting string issued by the server to the client upon first connecting is
```sh
$ ECE Senior Capstone IoT simulator
```

## Task 1: Data Flow
In order to write the data captured by ws_client.py, changes must be made to a function called by ws_client.py,
client.py

```sh
$ python ws_client.py -l data.txt
```



## Task 2: Analysis
After logging the data from ws_client.py into data.txt, the data can be analyzed by calling:
```sh
$ python analyze.py data.txt
```

Below is a table with values calculated from recorded temperature and occupancy data
|                      | Office | Lab1 | Class1 |
|----------------------|-------:|-----:|-------:|
| Median Temperature   |  22.99 | 21.0 |  26.96 |
| Temperature Variance |  32.41 | 2.31 | 139.81 |
| Median Occupancy     |    2.0 |  5.0 |   19.0 |
| Occupancy Variance   |   1.94 | 5.28 |  19.89 |


Below is a table with values calculated from the time-interval inbetween measurments
| Time inteval         | Office | Lab1 | Class1 |
|----------------------|-------:|-----:|-------:|
| Temperature Mean     |   2.89 | 2.87 |   2.99 |
| Temperature Variance |   7.43 | 9.33 |   8.41 |
| Occupancy Mean       |   2.89 | 2.87 |   2.99 |
| Occupancy Variance   |   7.43 | 9.33 |   8.41 |
| CO2 Mean             |   2.89 | 2.87 |   2.99 |
| CO2 Variance         |   7.43 | 9.33 |   8.41 |

Please note that these values have been hardcoded into this table with my collected data. If new data is used, this table will be out of date.




## Task 3: Design

## Task 4: Conclusions

