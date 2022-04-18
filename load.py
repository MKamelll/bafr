from Bafr import Bafr

def load_parser(raw):
    return raw.split(" ")[-3][:-1]

def load(params=None):
    cmd = "uptime"

    bafr = Bafr("load")
    bafr.set_cmd(cmd)
    bafr.set_parser(load_parser)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr.echo(end="\n")
