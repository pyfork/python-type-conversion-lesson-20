# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Instructor: Dr Angela Yu
# Journey start date: 12 Nov 2022

# Get two digit number from user

age = input('Enter a two digit number:\n')

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
# print(age_int_list)
# Add up integers in list
ail = age_int_list
ail_sum = sum(ail)
ail_sum_string = str(ail_sum)
# print(ail[0] + ail[1])
# print(sum(ail))
# print(sum(list(age_list_converted)))

# ANSWER
# two_digit_number = input("Type a two digit number: ")
# Example output
# 3 + 9 = 12
# 12

# string line
print(age_list[0] + " + " + age_list[1] + " = " + ail_sum_string)

# integer line
print(sum(ail))



# name = input("Your name?\n")

# print(type(name) +"\n")
# TypeError: unsupported operand type(s) for +: 'type' and 'str'

# print(type(name))

# name_len = len(name)
# print(type(name_len))

# print("your name has " + name_len + " characters.\n")
# TypeError: can only concatenate str (not "int") to str

# type conversion. typecasting.
# use str function
# or str(obj) ,, float(obj) ,, int(obj)
# converted_name_len = str(name_len)
# print("your name has " + converted_name_len + " characters.\n")
# text = 'The quick brown fox jumps over the lazy dog'
  
# Split the text wherever there's a space.
# words = text.split()
# print(words)

# words = text.split( )
# print(words)
# print(type(words))
# print(int(words))
# paragraph = 'The quick brown fox jumps over the lazy dog.' 


# age_text = str(age) not needed as input type is text maybe by ddefault
# print(age_text)
# print(type(age))
# print(type(age_text))
# Split the text wherever there's a full stop.
# a,b = paragraph.split('.')
# age_num = int(age)
# age_num_list = list(age_num)
# Display the results.
# print(a)
# print(b)`