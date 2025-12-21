# Problem Statement:
# Simulate a digital lock countdown by repeatedly reducing a number
# until it becomes a single digit.
#
# Rules:
# 1. Given a number, calculate the sum of its digits
# 2. Replace the number with this digit-sum
# 3. Repeat the process until the number becomes a single digit (0–9)
#
# Input:
# number    # integer value to be reduced
#
# Output:
# final_digit   # single digit result after repeated reductions



# Function to countdown the number till the number becomes single digit
def digital_lock_counter(num) :
  # This loop executes till the number becomes single digit. any positive number less than or equal to 9 is single digit
  while num > 9:
    total_sum = 0
    # Loop to calculate the sum of all digits in a number, by extracting last digit using modulo and adding it to new variable total_sum
    # then remove last digit from the number, Follow this steps till number becomes zero
    while num > 0:
      total_sum += num % 10
      num //= 10
    # Once the inner loop completes its execution, assign the value of total_sum to num
    num = total_sum
  # Prints the sum of all the digits in number until it becomes single digit
  print(num)

# Input statement.
num = int(input())
if num < 0:
  print("Please enter positive integer")
else:
  digital_lock_counter(num)