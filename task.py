import ntpath


class Task():
    def __init__(self, name, offset):
        self.name = name
        self.col_offset = offset
        self.counter = 0
    
    def get_cell(self, session_row):
        return self.col_offset, session_row + counter
    
    def __str__(self):
        return " ".join(str(s) for s in (self.name,self.col_offset,self.counter))

    def match_name(self, full_filename):
        name = ntpath.basename(full_filename)
        return name.lower().startswith(self.name.lower())

def generate_task_dict(task_names):
    task_data = {}
    for i, task in enumerate(task_names):
        task_data[task] = Task(task,1+i*2)
            
    return task_data

def match_task(dict, full_filename):
    for item in dict.values():
        if item.match_name(full_filename):
            return item
    print("Couldn't find a match for " + full_filename)
    
    for item in dict.values():
        print (item.name)
    return None
        
