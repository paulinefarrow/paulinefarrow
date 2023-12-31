# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# syntax error, missing parentheses for print function

print("Welcome to the error program")

# syntax error, unexpected indent

# syntax error, Missing parentheses in call to 'print'

print ("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# syntax error, unexpected indents
# syntax error, == used instead of =
# syntax error, can't convert text to an integer

age_str = "24" 


age = int(age_str) 

# syntax error, can only concatenate str (not "int")

print("I'm " + age_str + " years old.")

# Variables declaring additional years and printing the total years of age
# logical error, should be 3.5 not 3 years from now
years_from_now = 3.5

# syntax error, can't add str to int

total_years = age + years_from_now

# Syntax error, missing parentheses in call to 'print'

print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
# syntax error, name 'total' is not defined should be total_years
total_months = total_years * 12

# Syntax error, missing parentheses in call to 'print'

# syntax error, can only concatenate str (not "int") to str

print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer