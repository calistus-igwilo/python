import csv 

# Read a CSV file and write duplicate records to a file

hash = {}

with open('sent-total-40-50-hours.csv', 'r') as main:
    sent = csv.reader(main)
    for line in sent:
        hash[line[2]] = line[2]

with open('not-sent-3.csv', 'r') as file:
    content = csv.reader(file)

    for line in content:
        #print(f"{line[1]}\n")   
        if line[0] not in hash:
            with open('not-sent-4.csv', 'a') as items:
                items.write(f"{line[0]}, {line[1]}\n")
            #hash[line[1]] = ""        # set the duplicate value to empty string
        #hash[line[1]] = line[1]     # if not a duplicate, store value in hash table

    
        