##NOTE: Install "brightnessctl"

from Bafr import Bafr
from Grid import Grid
import os

def increase(value=3):
    cmd = "brightnessctl"
    flags = ["s", f"+{value}%"]

    bafr = Bafr("brightness.increase")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    
    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def decrease(value=3):
    cmd = "brightnessctl"
    flags = ["s", f"{value}%-"]

    bafr = Bafr("brightness.decrease")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    
    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def brightness_parser(raw):
    g = Grid(raw)
    for i in g:
        if "Current" in i:
            return i[3][1:-1]

def query():
    cmd = "brightnessctl"
    flags = ["i"]

    bafr = Bafr("brightness")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    bafr.set_parser(brightness_parser)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr.echo(end="\n")

def brightness(params=None):
    button = os.getenv("button")
    if button == "4":
        increase()
    elif button == "5":
        decrease()

    query()
