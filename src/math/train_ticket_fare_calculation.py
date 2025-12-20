# Problem Statement:
# Calculate train ticket fare based on distance and age with applicable discounts.
#
# Fare rules:
# 1. Base fare = distance × ₹2 per km
# 2. Senior citizen (age ≥ 60) → 30% discount
# 3. Child (age < 12) → 50% discount
# 4. Others → no discount
#
# Input:
# distance   # integer, distance traveled in km
# age        # integer, age of the passenger
#
# Output:
# fare       # final fare after applying any applicable discount
#
#
#---------------------------------------------------------------------
# Function to calculate ticket fare for all the age categories
def train_ticket_fare_calculation(distance, age):
  # Calculating fare with distance as 2rs per KM
  fare = distance * 2
  # Checking condition for age discount, if less than 12 -> 50%, and if more than 60 -> 30%
  if age < 12 :
    fare -= (fare*(50/100))
  elif age >= 60:
    fare -= (fare*(30/100))
  else:
    pass
  # Returning the calculated value
  return fare

# Input statements, takes two input from user distance and age
distance = int(input("Enter distance traveled in KM: "))
age = int(input("Enter the age: "))
#Input validation for negative values
if distance < 0 or age <0 :
  print("Please enter non negative values")
else:
  print(train_ticket_fare_calculation(distance, age))