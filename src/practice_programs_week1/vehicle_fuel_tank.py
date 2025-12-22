
def water_tank_overflow_detector(inflow_number, inflow):
  hours = 0
  max_volume = 50
  i=0
  while max_volume > 0 and i < inflow_number:
    if max_volume > 5: 
      max_volume -= inflow[i]
      hours += 1
      i += 1
    else:
      break
  
  return hours


inflow_number = int(input("Enter number of hours: "))
if inflow_number <= 0 :
  print("Inflow number should be a positive integer.")
else:
  inflow = list(map(int, input(f"Enter {inflow_number} water inflows: ").split()))
  
  if len(inflow) > inflow_number or len(inflow) < inflow_number:
    print(f"Enter exactly {inflow_number} space seperated values for water inflow.")
  else:
    print(water_tank_overflow_detector(inflow_number, inflow))


