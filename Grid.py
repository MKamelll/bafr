class Grid:
    def __init__(self, string, delim=" "):
        self.string = string
        self.delim = delim
        self.lines = [[j for j in i.split(delim) if len(j) > 0] 
                         for i in string.split("\n") if len(i) > 0]
    
    def __iter__(self):
        yield from self.lines

    def __str__(self):
        return f"{self.lines}"




