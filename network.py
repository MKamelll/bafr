from Bafr import Bafr
from Grid import Grid
import os

def network_parser(raw):
    g = Grid(raw)
    for i in g:
        if i[2] == "connected":
            return i[3]

def stength_parser(raw):
    g = Grid(raw)
    for i in g:
        if i[0] == "*":
            return f"{i[7]}%"

def query():
    cmd = "nmcli"
    flags = ["device"]

    bafr = Bafr("network")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    bafr.set_parser(network_parser)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr2 = Bafr("stength")
    cmd = "nmcli"
    flags = ["device", "wifi"]
    bafr2.set_cmd(cmd)
    bafr2.set_cmd_flags(flags)
    bafr2.set_parser(stength_parser)

    if not bafr2.run():
        bafr2.eecho(end="\n")
        bafr2.exit()

    bafr.echo(end=" ")
    bafr2.echo(end="\n")

def device_name_parser(raw):
    g = Grid(raw)

    for i in g:
        if i[2] == "connected":
            return i[0]

def restart():
    cmd = "nmcli"
    flags = ["device"]

    bafr = Bafr("network.restart")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    bafr.set_parser(device_name_parser)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    device_name = bafr.get_parsed_data()

    disconnect_flags = flags + ["disconnect", device_name]
    connect_flags = flags + ["connect", device_name]

    bafr.set_cmd_flags(disconnect_flags)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()
    
    bafr.set_cmd_flags(connect_flags)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def network(params=None):
    button = os.getenv("button")
    if button == "1":
        restart()

    query()
   
