class Task():
    def __init__(self, name, offset):
        self.name = name
        self.col_offset = offset
        self.counter = 0
    
    def get_cell(self, session_row):
        return self.col_offset, session_row + counter
    
    def __str__(self):
        return " ".join(str(s) for s in (self.name,self.col_offset,self.counter))
