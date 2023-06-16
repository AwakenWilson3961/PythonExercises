# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


'''

Expected Output:

Original String is  pynative
Printing only even index chars
p
n
t
v

'''

# Their output/build/solution 

# Accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# Using list slicing
# Convert string to list
# Pick only even index chars

x = list(word)
for i in x[0::2]:
    print(i)
