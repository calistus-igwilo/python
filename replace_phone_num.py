import csv 

# Read a CSV file and replace empty cells in a named column with a default number

hash = {}
default_phone_num = "1234567890"

with open('testing2.csv', 'r') as file:
    content = csv.reader(file)

    for line in content:
        if line[6] == " " or line[6] == '':
            line[6] = default_phone_num
            with open('phone_update.csv', 'a') as items:
                items.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{line[6]}\n")
        with open('phone_update.csv', 'a') as items:
            items.write(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{line[6]}\n")
           
    
        