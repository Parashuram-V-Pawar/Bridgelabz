# Problem Statement:
# An online shopping platform applies discounts based on the total order amount.
#
# Discount rules:
# - If total amount ≥ 5000 → apply 20% discount
# - If total amount ≥ 3000 → apply 10% discount
# - If total amount ≥ 1000 → apply 5% discount
# - Otherwise → no discount
#
# Only the highest applicable discount should be applied.
#
# Input:
# amount   # total order amount
#
# Output:
# payable_amount   # final amount after applying discount
#
# Function to apply the discount on the bill amount
def online_order_discount_engine(amount) :
  discount = 0
  # If amount is >= 5000, 20% discount will be applied
  if amount >= 5000:
    discount += 20
  # If amount is >=3000 and < 5000, 10% discount is applied
  elif amount >= 3000 and amount < 5000:
    discount += 10
  # If amount is >=1000 and < 3000, 5% discount is applied
  elif amount >= 1000 and amount < 3000:
    discount += 5
  # If amount is <1000 no discount is applied
  else :
    pass
  # Once the discount is applied we need to calculate the bill by reducing the discounted price
  total = int(amount - (amount*(discount/100)))
  # Discounted price is returned
  return total

# Input statement
amount = int(input("Enter total bill amount: "))

# Checking whether the amount is negative value. 
# If it is non-negative calling the function and passing amount as parameter, and then printing the received value
if amount < 0:
  print("Bill amount cannot be negative")
else:
  print(online_order_discount_engine(amount))
