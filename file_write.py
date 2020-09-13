from pathlib import Path
import argparse

# other code; argparse sets P.log value from command line as in ws_client.py


#Set arguments containter
p = argparse.ArgumentParser(description="WebSocket client")
#Define arguments
p.add_argument("-l", "--log", help="file to log JSON data")
p.add_argument("-host", help="Host address", default="localhost")
p.add_argument("-port", help="network port", type=int, default=8765)
p.add_argument(
    "-max_packets",
    help="shut down program after total packages received",
    type=int,
    default=100000,
)
#Parse for arguments
P = p.parse_args()

filename = Path(P.log).expanduser()

print(filename)

# other code

file = filename.open("a")

# other code

#file.write(txt + "\n")
#file.flush()

# other code

file.close()
