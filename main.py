# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Instructor: Dr Angela Yu
# Journey start date: 12 Nov 2022

# Get two digit number from user. Input function returns string characters.
age = input('Enter a two digit number:\n')

# Use substring/slicing method
# print(age[0] + age[1])

# Convert input to integers
first_digit = int(age[0])
second_digit = int(age[-1])

# Return sum of integers
print(first_digit + second_digit)