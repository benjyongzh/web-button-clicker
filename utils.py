import csv
import glob
import os
from datetime import datetime
import time

def get_current_file_count(target_dir):
        if os.path.exists(target_dir):
                files = os.listdir(target_dir)
                return len(files)
        else:
                return 0
        
def wait_for_download(timeout, target_dir, nfiles):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
            time.sleep(1)
            dl_wait = False
            if os.path.exists(target_dir):
                    files = os.listdir(target_dir)
                    if len(files) == nfiles:
                            dl_wait = True
                    for fname in files:
                            if fname.endswith('.crdownload'):
                                    dl_wait = True
            else:
                    dl_wait = True
            seconds += 1

def format_filename(file_name:str):
    currentDateTime = datetime.now()
    datetime_filename_format = "%Y%m%d-%H%M%S"
    date_text = currentDateTime.strftime(datetime_filename_format)
    return date_text + "_" + file_name

def add_id_rows(filename, filename_postpend_string):

    with open(filename+".csv") as inp, open(filename+filename_postpend_string+".csv", 'w') as out:
        reader = csv.reader(inp)
        writer = csv.writer(out, delimiter=',')
        #No need to use `insert(), `append()` simply use `+` to concatenate two lists.
        writer.writerow(['id'] + next(reader))
        #Iterate over enumerate object of reader and pass the starting index as 1.
        writer.writerows([i] + row for i, row in enumerate(reader, 1))
        

def get_latest_file(folder_path:str):
    path:str = folder_path + "*"
    files = glob.glob(path)
    return max(files, key=os.path.getctime)
