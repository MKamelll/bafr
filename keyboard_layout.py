from Bafr import Bafr

def layout_parser(raw):
    return [i for i in raw.split("\n") if len(i) > 0][2].split(" ")[-1]

def keyboard_layout(params=None):
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
