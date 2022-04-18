from Bafr import Bafr

def weather_celius(raw):
    return raw.split(" ")[-1][:-1]

def weather(params=None):
    if not params: params = []
    location = params[0] if len(params) > 0 else ""
    
    cmd = "curl"
    flags = [f"wttr.in/{location}?format=3"]
    bafr = Bafr("weather")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags)
    bafr.set_parser(weather_celius)

    if not bafr.run():
        bafr.eecho(end="\n")
        bafr.exit()

    bafr.echo(end="\n")
