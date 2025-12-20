# Problem Statement:
# A traffic signal cycles every second with the following rules:
# - Seconds 1 to 30   → RED
# - Seconds 31 to 45  → YELLOW
# - Seconds 46 to 90  → GREEN
#
# Given a time T (in seconds), determine and print the signal color.
#
# Input:
# T
#
# Output:
# RED / YELLOW / GREEN


# Function to demonstrate the traffic signal 
def traffic_signal_simulator(time):

  # Using modulo on time to check for next signal cycle if input is >90.
  t = (time%90)

  # Condition to check if t is in between 1 - 30
  if t in range(1,31):
    print("RED")
  
  # Condition to check if t is in between 31 - 45
  elif t in range(31,46):
    print("YELLOW")

  # Condition to check if t is in between 46 - 90
  # Have used t==0 because 90%90 is 0
  elif t in range(46, 91) or t == 0:
    print("GREEN")

# Taking inout from User
time = int(input())

# Checking if user entered positive integer and non zero value
if time <= 0 :
  print("Please enter a positive number")
else: 
  traffic_signal_simulator(time)