import csv

# /home/benjyongzh/Downloads/pg-practice
def add_id_rows(filename, filename_postpend_string):

    with open(filename+".csv") as inp, open(filename+filename_postpend_string+".csv", 'w') as out:
        reader = csv.reader(inp)
        writer = csv.writer(out, delimiter=',')
        #No need to use `insert(), `append()` simply use `+` to concatenate two lists.
        writer.writerow(['id'] + next(reader))
        #Iterate over enumerate object of reader and pass the starting index as 1.
        writer.writerows([i] + row for i, row in enumerate(reader, 1))