from pathlib import Path

# other code; argparse sets P.log value from command line as in ws_client.py

filename = Path(P.log).expanduser()

# other code

file = filename.open("a")

# other code

file.write(txt + "\n")
file.flush()

# other code

file.close()
