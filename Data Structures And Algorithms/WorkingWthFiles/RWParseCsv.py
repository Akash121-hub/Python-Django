import csv

with open('yelp.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader) # To Skip the first value ( in case if we have column name)
    with open("new_file","w") as new_csv_file:
        new_csv_file_writer = csv.writer(new_csv_file,delimiter='-') # creating new file and writing rows into it
        for line in csv_reader:
            new_csv_file_writer.writerow(line)

            # print(line[0])