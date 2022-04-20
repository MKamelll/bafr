#!/usr/bin/env python3

from date import date
from volume import volume
from weather import weather
from load import load
from memory import memory
from keyboard_layout import keyboard_layout
from network import network
from cli import cli

import sys

available_modules = {   "date"   : date,
                        "volume" : volume,
                        "weather": weather,
                        "load"   : load,
                        "memory" : memory,
                        "keyboard_layout": keyboard_layout,
                        "network": network
                    }
    
def assert_available(module):
    if module not in available_modules:
        print("Available modules =>")
        for i in available_modules.keys():
            print(f"\t {i}")
        sys.exit(1)

def main():
    module, params = cli()
    assert_available(module)
    available_modules[module](params)

if __name__ == "__main__":
    main()
