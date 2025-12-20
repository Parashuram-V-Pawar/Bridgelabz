# Problem Statement:
# Employee salary calculation based on deductions for late and absent days:
# 1. Basic salary is given.
# 2. If late_days > 5, deduct 5% of basic salary.
# 3. If late_days > 10, deduct 10% of basic salary.
# 4. If absent_days > 2, deduct an additional 5% of basic salary.
#
# Input:
# salary       # basic salary
# late_days    # number of days employee was late
# absent_days  # number of days employee was absent
#
# Output:
# final_salary  # salary after applying all deductions

# Function to perform salary deductions
def salary_deduction_system(basic_salary, late_days, absent_days) :
  deduction = 0

  # Checking condition if late_days > 5 and  late_days <= 10, if yes apply 5% deduction
  if late_days > 5 and late_days <= 10:
    deduction += 5

  # Checking condition if late_days > 10, if yes apply 10% deduction
  elif late_days > 10 :
    deduction += 10

  # If both the conditons fail we don't apply deduction and go ahead
  else:
    pass

  # Checking if absent_days are more than 2, if yes apply 5% deduction
  if absent_days > 2:
    deduction += 5


  # Calculating the payable salary by deducting the deductions.
  # First we calculate the amount to be deducted and then calculate the payable_salary.
  final_salary = int(basic_salary - (basic_salary * (deduction/100)))

  # Returning the payable_salary
  return final_salary

# Input statements
basic_salary = int(input())
late_days = int(input())
absent_days = int(input())


# Ensuring basic_salary, late_days, absent_days are not negative values and also basic_salary should not be 0.
if(basic_salary <= 0 and late_days < 0 and absent_days < 0) :
  print("Basic salary cannot be 0 and please enter positive values for all inputs")
else:
  print(salary_deduction_system(basic_salary, late_days, absent_days))