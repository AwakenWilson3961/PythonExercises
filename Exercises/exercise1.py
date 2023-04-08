# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

'''
Example 

number1 = 20
number2 = 30

Expected Output: The result is 600

number1 = 40
number2 = 30

Expected Output: The result is 70

'''

# My output/build/solution

user_input_1 = int(input('Enter any number'))

print(user_input_1)

user_input_2 = int(input('Enter any second number'))

print(user_input_2)

if user_input_1 * user_input_2 > 1000:
	print('The result is: ' , user_input_1 + user_input_2 )
else:
	if user_input_1 * user_input_2 < 1000:
		print('The result is: ' , user_input_1 * user_input_2 )
