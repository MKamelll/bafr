import sys

USAGE = "Usage: bafr <module> [options]"

def print_usage():
    print(USAGE)

def cli():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_usage()
        sys.exit(0)


    module = sys.argv[1]
    params = sys.argv[2:]

    return (module, params)
    
