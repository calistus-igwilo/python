"""
From the given file name:
    filename = 'view.jpg'
extract extension and print it to the console
"""

filename = 'veiw.jpg'
print(filename[-3:])
# or
print(filename[5:])

# remove spaces
"""
From the following text
    string = '1 0 0 1 0 1'
remove spaces using slicing. Then convert the result to 
decimal notation and print to the console as shown below:

Number found: 37
"""

string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Number found: {number}')