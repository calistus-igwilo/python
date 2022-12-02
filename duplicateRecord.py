
# Read a CSV file and write duplicate records to a file

hash = {}
with open('nitda-total.csv', 'r') as file:
    content = file.read().splitlines()


for line in content:
    values = line.split(',')
    print(values[1], values[2])     # get the email address and firstname
   
    if values[1] in hash:
        with open('duplicates.csv', 'a') as duplicate:
            duplicate.write(line)
            duplicate.write('\n')   # add a new line
        hash[values[1]] = ""        # set the duplicate value to empty string
    hash[values[1]] = values[1]     # if not a duplicate, store value in hash table

    
        