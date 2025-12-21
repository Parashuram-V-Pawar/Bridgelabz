# Problem Statement:
# Check whether a given number is a palindrome (number mirror).
#
# Definition:
# A number is called a palindrome if it remains the same
# when its digits are reversed.
#
# Input:
# number    # integer to be checked
#
# Output:
# PALINDROME        # if original number equals reversed number
# NOT PALINDROME    # otherwise
#
# Function to check given number is palindrome or not palindrome
def number_mirror_validator(number):
  palindrome = 0
  while number > 0:
    # We extract the last digit and store it in remainder using modulo
    remainder = number % 10
    # Multiply the palindrome by 10 and add the remainder the to it
    palindrome = (palindrome * 10) + remainder
    # Use integer division to remove the last digit from the number
    number = number // 10
  
  # Returning the palindrome. 
  return palindrome

# Input statement, validating input to be positive number
number = int(input("Enter a number: "))
if number < 0:
  print("Please enter the positive number")
else:
  # statement passes the number to the palindrome function and expects the reverse number
  # once received it will check for similarity, if both the numbers are same prints "PALINDROME" else "NOT PALINDROME"
  if number == number_mirror_validator(number):
    print("PALINDROME")
  else:
    print("NOt PALINDROME")