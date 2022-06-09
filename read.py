# with open('fizzbuzz.py') as f:
#     read_data = f.read()

# print(read_data)


with open('fizzbuzz.py') as f:
    print(f.readline())

"""
Write a program that reads playway.txt file containing Playway stock data,
and then calculates the average closing price (3-day average).
    Playwright.txt contents:
Date,Open,High,Low,Close,Volume
2020-04-01,302,314,300,310,12940
2020-04-02,310,315,305,313,10311
2020-04-03,313,318.5,312,318,12372


Print result to the console as show below

Expected result

"""
with open('Playwright.txt', 'r') as file:
    lines = file.read().splitlines()

close = []
for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))
result = sum(close)/len(close)
print(f'{result :.2f}')


"""
Read the currencies.txt file. Each line has different currency pair.
Create a list with the names of currency pairs containing the 'USD' 
symbol.
"""
pairs = []
with open('currencies.txt', 'r') as file:
    lines = file.read().splitlines()

symbols = [symbol for symbol in lines if 'USD' in symbol]
print(symbols)


"""
The playway.csv file contains Playway's listing for March 2020. This file
was loaded as follows to the content variable:
    with open('playway.csv', 'r') as file:
        content = file.read().splitlines()

Transform the contents of the file to get a dictionary containing two
keys 'Date' and 'Close'. The values for these keys will be respectively,
lists consisting of all dates and closing prices. Convert closing prices
to float type and print this dictionary to the console as shown belos

Formatted result:

"""
with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
date = []
close = []
for idx, line in enumerate(content):
    if idx > 0:
        date.append(line.split(',')[0])
        close.append(float(line.split(',')[-2]))
print(date)
print(close)

with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
data = [(line.split(',')[0], line.split(',')[4]) for line in content ]
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
    }
print(result)


"""
The playway.csv file contains Playway's listing for March 2020. This 
file was loaded as follows to the content variable
    with open('playway.csv', 'r') as file:
        content = file.read().splitlines()
Find the highest volume for a given month and print the result tothe console

Expected result
    Max Vol: 100412
"""
with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
volumes = [(line.split(',')[-1]) for line in content[1:]]
volumes = [int(vol) for vol in volumes]
max_vol = max(volumes)
print(f'Max Vol: {max_vol}')

"""
Find the date with the highest volume

Expected result
    Date: 2020-03-13
"""
with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
data = [(line.split(',')[0], line.split(',')[-1]) for line in content[1:] ]
dic = {item[0]: int(item[1]) for item in data}
max_vol = max(dic, key = lambda x: dic[x])
print(dic)
print(max_vol)