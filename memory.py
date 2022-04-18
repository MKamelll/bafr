from Bafr import Bafr

def memory_parser(raw):
    total = [i for i in raw.split(" ") if len(i) > 0][1*6+0][:-2]
    used  = [i for i in raw.split(" ") if len(i) > 0][1*6+1][:-2]
    return str(int(float(used) * 100 / float(total))) + "%"

def memory(params=None):
    cmd = "free"

    bafr = Bafr("memory")
    bafr.set_cmd(cmd)
    bafr.set_parser(memory_parser)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr.echo(end="\n")
