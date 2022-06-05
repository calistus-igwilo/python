"""
The following set is given:

    subjects = {'mathematics', 'biology'}
Using the appropriate method add 'english' to the set. 
in response print subjets to the console as shown below

{'biology', 'mathematics', 'english'}
Note: Remember that set is an unordered data structure. You may 
get different order of the items
"""

subjects = {'mathematics', 'biology'}
subjects.add('english')
print(subjects)

"""
The following text is given:
    
    text = 'Programming in python.'
follow the next steps:
1. Change all letters to lowercase
2. Delete spaces and period
3. Create a set consisiting of all letters in the text and
    assign to letters variable
4. Using the appropriate method for sets, remove all vowels from
    the letters set.

    vowels = {'a', 'e', 'i', 'o', 'u'}
5. Print the number of items in the letters set as shown below:
"""

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower().strip('.').replace(' ', '')
letters = set(text)
consonats = letters.difference(vowels)
print(consonats)
print(f'Number of items: {len(consonats)}')


"""
In mathematics, the symmetric difference of two sets is the set of elements
which are in either of the sets, but not in their intersection
The following sets are given:

    A = {2, 4, 6, 8}
    B = {4, 10}
Using the appropriate method, extract the symmetrical difference of 
sets A and B and print result to the console as shown below:

    Symetric difference: {2, 6, 8, 10}
"""

A = {2, 4, 6, 8}
B = {4, 10}

intersect = A.intersection(B)
a_diff = A.difference(intersect)
b_diff = B.difference(intersect)
sym_diff1 = a_diff.union(b_diff)
print(f'Symetric difference 1: {sym_diff1}')
# OR
sym_diff = A.symmetric_difference(B)
print(f'Symetric difference: {sym_diff}')

print(set(sym_diff) == set(sym_diff1))


"""
We have two sets of customer IDs
    ad1_id = {'001', '002', '003'}
    ad2_id = {'002', '003', '007'}
Each set stores the id of the customers who made the purchase based on
the specific ad. We have two ads. Each customer can use the offer only
twice in campaign. Choose the ID of the customers to whom you can send
another ad (or ids that only appeared once in both sets)

Expected result:
    Selected ID: { '007', '001'}
Note: Remember that the set is an unordered data structure. You may get 
a different order of items than expected result.
"""

ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}

sym_diff3 = ad1_id.symmetric_difference(ad2_id)
print(f'Selected ID: {sym_diff3}')