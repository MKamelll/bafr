from Bafr import Bafr
from Grid import Grid

def network_parser(raw):
    g = Grid(raw)
    for i in g:
        if i[2] == "connected":
            return f"up:{i[3]}"

def stength_parser(raw):
    g = Grid(raw)
    for i in g:
        if i[0] == "*":
            return f"{i[7]}%"

def network(params=None):
    if not params: params = []

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


