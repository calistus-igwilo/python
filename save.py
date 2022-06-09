"""
Generate all even numbers from 2 to 18 inclusive. Then write each number 
on a separate line fo the file called num.txt
"""
numbers = []
for i in range(2, 20, 2):
    numbers.append(i)
print(numbers)

with open('num.txt', 'w') as file:
    for num in numbers:
        file.write(str(num) + '\n')


"""
The follwoing dictionary is given:
    stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
save to stocks.json using the json package. Set the indent to 4
"""
import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)


"""
The following list are given:

headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

Save the above data to the users.csv file (file in csv format - comma-separated
values)as shown below

"""
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('users.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')