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

# My output/build/solution

userInput = str(input('Enter any word:'))

print('Original String is', ' ', userInput)

print('Printing only even index chars')

for i in userInput:
    print(i)

print('Done...')