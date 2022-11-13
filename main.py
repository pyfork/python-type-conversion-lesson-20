# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Instructor: Dr Angela Yu
# Journey start date: 12 Nov 2022

# Get two digit number from user
age = input('Enter a two digit number:\n')

# 2nd approach
# two_digit_number = input("Type a two digit number: ")
# age = two_digit_number

# Convert digits to list - default is string list
age_list = list(age)

# Show string list
# print(age_list)

# Convert string list members to integer
age_list_converted = map(int,age_list)

# Convert integer list map to integer list
age_int_list = list(age_list_converted)

# Show integer list
# print(age_int_list)

# Add up integers in list
ail = age_int_list
ail_sum = sum(ail)

# Convert total to string
ail_sum_string = str(ail_sum)

# Alternate approaches
# print(ail[0] + ail[1])
# print(sum(ail))
# print(sum(list(age_list_converted)))

# ANSWER string line
print(age_list[0] + " + " + age_list[1] + " = " + ail_sum_string)

# ANSWER integer line
print(sum(ail))

# ANSWER REQUIREMENT
# two_digit_number = input("Type a two digit number: ")
# Example output
# 3 + 9 = 12
# 12