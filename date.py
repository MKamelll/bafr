from Bafr import Bafr

def date(params=None):
    cmd = "date"
    flags = ["+%I:%M %p ~ %y-%m-%d"]
    bafr = Bafr("date")
    bafr.set_cmd(cmd)
    bafr.set_cmd_flags(flags) 
    
    if not bafr.run():
        bafr.eecho()
        bafr.exit()

    bafr.echo()

