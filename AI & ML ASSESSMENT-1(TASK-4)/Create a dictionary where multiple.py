# Create a dictionary where multiple
# values are associated with a key
word_freq = {'is'   : [1, 3, 4, 8, 10],
             'at'   : [3, 10, 15, 7, 9],
             'test' : [5, 3, 7, 8, 1],
             'this' : [2, 3, 5, 6, 11],
             'why'  : [10, 3, 9, 8, 12] }


# Get multiple values of a key as list
value_list = word_freq['is']

print('Values of key "is" are:')
print(value_list)