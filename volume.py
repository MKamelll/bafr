from Bafr import Bafr

def parse_volume_get(raw):
    return "".join([i.strip().split(" ")[4][1:4] for i in raw.split("\n") 
                    if i.strip().startswith("Front Left")])

def volume(params=None):
    cmd = "amixer"
    flags = ["get", "Master"]
    
    bafr = Bafr("volume")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags) 
    bafr.set_parser(parse_volume_get)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr.echo(end="\n")

