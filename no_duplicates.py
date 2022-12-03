import csv 

# Read a CSV file and write duplicate records to a file

hash = {}

with open('duplicates.csv', 'r') as main:
    duplicate = csv.reader(main)
    for line in duplicate:
        hash[line[0]] = line[0]

with open('nitda-total.csv', 'r') as file:
    content = csv.reader(file)

    for line in content:
        #print(f"{line[1]}\n")   
        if line[1] not in hash:
            with open('no-duplicates.csv', 'a') as items:
                items.write(f"{line[1]}, {line[2]}\n")
            #hash[line[1]] = ""        # set the duplicate value to empty string
        #hash[line[1]] = line[1]     # if not a duplicate, store value in hash table

    
        