import csv

def get_score(filename):    
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:            
            if len(row) > 0 and row[0] == 'Score:':
                return row[1]
    return None
