#!/usr/bin/env python3
"""
WebSockets client

This program receives simulated data for multiple rooms, with multiple sensors per room.

The default behavior is to only access the computer itself by parameter "localhost"
so that no firewall edits are needed.

The port number is arbitrary, as long as the server and client are on the same port all is well.

Naturally, the server ws_server.py must be started before this client attempts to connect.
"""

import argparse
import asyncio
from aiofile import AIOFile 

from sp_iotsim.client import main

#async def main(file):
#    async with AIOFile(file, 'w+') as afp:
#        await afp.wr




if __name__ == "__main__":
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

    #Recieving from ws_server.py
    try:
        asyncio.run(main(P.port, P.host, P.max_packets, P.log))
    except KeyboardInterrupt:
        print("Terminating Client")
        
