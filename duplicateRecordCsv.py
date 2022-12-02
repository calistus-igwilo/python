import csv 

# Read a CSV file and write duplicate records to a file

hash = {}
with open('nitda-total.csv', 'r') as file:
    content = csv.reader(file)


    for line in content:   
        if line[1] in hash:
            with open('duplicates.csv', 'a') as duplicate:
                duplicate.write(line)
                duplicate.write('\n')   # add a new line
            hash[line[1]] = ""        # set the duplicate value to empty string
        hash[line[1]] = line[1]     # if not a duplicate, store value in hash table

    
        