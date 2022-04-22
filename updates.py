from Bafr import Bafr
from Grid import Grid

def updates_parser(raw):
    g = Grid(raw)
    return len(g) if len(g) > 0 else ""

def updates(params=None):
    if not params: params = []

    pkg_manger = params[0]
    update_cmd = params[1:]

    cmd = pkg_manger
    flags = update_cmd

    bafr = Bafr("updates")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    bafr.set_parser(updates_parser)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr.echo(end="\n")

