# Problem Statement:
# Process exam results for a student based on marks in 5 subjects.
#
# Rules:
# 1. If any mark is less than 35 → student FAILS
# 2. Else if average of all 5 subjects ≥ 75 → student gets DISTINCTION
# 3. Else → student PASSES
#
# Input:
# m1 m2 m3 m4 m5   # marks for 5 subjects (integers)
#
# Output:
# FAIL / PASS / DISTINCTION   # based on above rules
#
# Function to check the result
def exam_result_processor(marks):
  total = 0
  # Iterating all elements in list 
  for m in marks:
    # check condition with individual element if any value is < 35 then returns FAIL
    # Else the marks are added to the total
    if m < 35:
      return "FAIL"
    else:
      total += m
  # Once we get the total, Average is calculated by dividing it with number of elements in list
  avg = total/len(marks)
  # If average is 75 and above returns "DISTINCTION", else returns "PASS"
  if avg >= 75 :
    return "DISTINCTION"
  else:
    return "PASS"
  
# Input statement, takes input from the user, splits where space is present and maps as individual element in list
marks = list(map(int, input("Enter marks for 5 subjects: ").split()))
# Input validation, checks if the input has only 5 marks
if len(marks) == 5 :
  print(exam_result_processor(marks))
else :
  print("Enter marks only for 5 subjects")
