import glob
import os

stats_folder = "C:/Program Files (x86)/Steam/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats/*.csv"



def num_files():
    list_of_files = glob.glob(stats_folder) # * means all if need specific format then *.csv
    return(len(list_of_files))

def latest_file():
    list_of_files = glob.glob(stats_folder) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file
