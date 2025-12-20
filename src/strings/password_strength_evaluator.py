# Problem Statement:
# Given a password string:
# 1. Must contain at least 1 digit
# 2. Must contain at least 1 uppercase letter
# 3. Length of password must be >= 8
# Print STRONG if all conditions are satisfied, otherwise print WEAK.

# Input:
# password

# Output:
# STRONG or WEAK

# Function to check password strength
def password_strength_checker(password):
  is_digit = False
  is_uppercase = False

  # Loop to check each character in password
  for p in password :

    # Condition checks if the character is uppercase
    if p.isupper():
      is_uppercase = True

    # Condition checks if the character is digit
    elif p.isdigit():
      is_digit = True
  
  # Condition to check if the length is >= 8 and has atleast 1 digit and uppercase letter
  if(len(password)>=8 and is_uppercase and is_digit) :
    print("STRONG")
  else :
    print("WEAK")


# Taking input from user
password = input()

# Calling function and passing password as argument
password_strength_checker(password)