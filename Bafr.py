import subprocess
import sys

class Cmd:
    def __init__(self, cmd, flags):
        self.cmd = cmd
        self.flags = flags
        self.error_code = 0
        self.error_str = None
        self.result = None
    
    def exec(self):
        result = subprocess.run([self.cmd] + self.flags, capture_output=True, text=True)
        
        if result.returncode > 0:
            self._set_error_code(result.returncode)
            self._set_error_str(result.stderr)
            return False
        
        self.result = result.stdout
        
        return True
    
    def _set_error_code(self, returncode):
        self.error_code = returncode

    def _set_error_str(self, error_str):
        self.error_str = error_str

    def get_error_code(self):
        return self.error_code

    def get_error_str(self):
        return self.error_str

    def get_result(self):
        return self.result


class Bafr:
    def __init__(self, mod_name=None):
        if not mod_name:
            mod_name = "bafr"
        self.mod_name = mod_name
        self.cmd = None
        self.flags = []
        self.parser = None
        self.raw = None
        self.parsed_data = None
        self.attributes = {}
        self.signal_num = None

        ####################################
        self.error_code = 0
        self.error_str = None

    def set_cmd(self, cmd):
        self.cmd = cmd

    def set_parser(self, parser):
        self.parser = parser

    def set_cmd_flags(self, flags):
        self.flags = flags

    def run(self):
        cmd = Cmd(self.cmd, self.flags)
        if not cmd.exec():
            self.error_code = cmd.get_error_code()
            self.error_str = cmd.get_error_str()
            return False
        
        self._set_raw(cmd.get_result())
        
        if not self.parser:
            self.parsed_data = self.raw
        else:
            self.parsed_data = self.parser(self.raw)
        
        return True

    def _set_raw(self, raw_data):
        self.raw = raw_data

    def get_parsed_data(self):
        return self.parsed_data

    def get_error_code(self):
        return self.error_code
    
    def get_error_str(self):
        return self.error_str
    
    def set_attr(self, attr, val):
        self.attributes[attr] = val
    
    def get_attr(self, attr):
        if attr not in self.attributes: return None

        return self.attributes[attr]

    def echo(self, end=""):
        print(self.get_parsed_data(), end=end)

    def eecho(self, end=""):
        print(f"[bafr.{self.mod_name}.ERR]: {self.get_error_str()}", file=sys.stderr, end=end)

    def exit(self):
        sys.exit(self.get_error_code())

    def set_signal_num(self, num):
        self.signal_num = num

    def get_signal_num(self):
        return self.signal_num

    def signal_i3blocks(self):
        if not self.get_signal_num(): return False
        
        flags = [f"-{self.get_signal_num()}", "i3blocks"]
        cmd = Cmd("pkill", flags)

        if not cmd.exec():
            self.error_code = cmd.get_error_code()
            self.error_str = cmd.get_error_str()
            return False
        
        return True

