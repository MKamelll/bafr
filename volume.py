from Bafr import Bafr
from Grid import Grid 
import os

def parse_volume(raw):
    g = Grid(raw)
    for i in g:
        if i[0] == "Front":
            if i[-1] == "[on]":
                return i[-2][1:-1]
    return "mute"

def increase(value=3):
    cmd = "amixer"
    flags = ["-q", "sset", "Master", f"{value}%+"]

    bafr = Bafr("volume_increase")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def decrease(value=3):
    cmd = "amixer"
    flags = ["-q", "sset", "Master", f"{value}%-"]

    bafr = Bafr("volume_decrease")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def mute():
    cmd = "amixer"
    flags = ["-q", "sset", "Master", "mute"]

    bafr = Bafr("volume_mute")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def unmute():
    cmd = "amixer"
    flags = ["-q", "sset", "Master", "unmute"]

    bafr = Bafr("volume_unmute")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

def query():
    cmd = "amixer"
    flags = ["get", "Master"]
    
    bafr = Bafr("volume")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags) 
    bafr.set_parser(parse_volume)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr.echo(end="\n")

def volume(params=None):
    buttons = { "1": mute, "3": unmute, "4": increase, "5": decrease }
    
    if button := os.getenv("button"):
        if button in buttons:
            buttons[button]()

    query()

