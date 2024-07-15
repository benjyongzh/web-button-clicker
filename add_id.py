import csv
import argparse

# /home/benjyongzh/Downloads/pg-practice

parser = argparse.ArgumentParser(description="Script that adds an 'id' column to a .csv file")
parser.add_argument("--filename", required=True, type=str, help="Enter the filename to add running id column to.")
args = parser.parse_args()

with open(args.filename+".csv") as inp, open(args.filename+"_with-id"+".csv", 'w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')
    #No need to use `insert(), `append()` simply use `+` to concatenate two lists.
    writer.writerow(['id'] + next(reader))
    #Iterate over enumerate object of reader and pass the starting index as 1.
    writer.writerows([i] + row for i, row in enumerate(reader, 1))