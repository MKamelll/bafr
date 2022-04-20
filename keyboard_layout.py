from Bafr import Bafr
from Grid import Grid
import os

def layout_parser(raw):
    g = Grid(raw)
    for i in g:
        if i[0] == "layout:":
            return i[1]

def set_layout(layout):
    cmd = "setxkbmap"
    flags = [layout]

    bafr = Bafr("set_layout")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def query():
    cmd = "setxkbmap"
    flags = ["-query"]

    bafr = Bafr("keyboard_layout")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    bafr.set_parser(layout_parser)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()
    
    bafr.echo(end="\n")

def keyboard_layout(params=None):
    button = os.getenv("button")
    if button == "1":
        set_layout("us")
    elif button == "3":
        set_layout("ara")

    query()
