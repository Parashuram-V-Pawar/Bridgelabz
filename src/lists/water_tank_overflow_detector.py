# Problem Statement:
# Simulate a water tank filling system with overflow detection.
#
# Rules:
# 1. Tank capacity is fixed at 1000 liters
# 2. Water flows into the tank every minute as per given inflows
# 3. Stop filling immediately if total volume exceeds capacity
# 4. Print the minute number at which overflow occurs
#
# Input:
# N                 # number of minutes / inflow readings
# inflow1 inflow2 ... inflowN   # liters of water entering each minute
#
# Output:
# overflow_minute   # the minute when the tank first overflows
#
# Function to check if the water tank fills in how much time.
def water_tank_overflow_detector(inflow_number, inflow):
  minute = 0
  # Initially the capacity of the water tank is 1000ltrs
  max_volume = 1000
  i=0
  # Checking condition if capacity of tank is not full and ensuring the loop only runs for number of inflows entered
  while max_volume > 0 and i < inflow_number:
    # reducing the capacity for each iteration by received inflow and increasing minute everytime capacity is reduced
    # i is used to iterate over items in list and increasing it everytime to point it to next item
    max_volume -= inflow[i]
    minute += 1
    i += 1
  # In the end returning the minute value if capacity is 0 or less, else returning "NO OVERFLOW"
  if max_volume > 0:
    return "NO OVERFLOW"
  else:
    return minute

# Input statement, Expecting the integer value
inflow_number = int(input("Enter number of water inflows: "))
# If the value entered is 0 or less then prints error message, else proceeds further
if inflow_number <= 0 :
  print("Inflow number should be a positive integer.")
else:
  # List is created and accepts the items in single line seperated by space
  inflow = list(map(int, input(f"Enter {inflow_number} water inflows: ").split()))
  # Confdition checks if list items entered are less than no of water inflows or more than water inflows it prints error message
  # If the condittion is met, calls the water_tank_overflow_detector function to track the number of minutes and prints it
  if len(inflow) > inflow_number or len(inflow) < inflow_number:
    print(f"Enter exactly {inflow_number} space seperated values for water inflow.")
  else:
    print(water_tank_overflow_detector(inflow_number, inflow))

