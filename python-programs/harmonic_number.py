num = int(input("Enter number: "))
harmonic = 0
if(num <=0 ):
  print("Please enter number greater than 0.")
else :
  for i in range(1, num+1) :
    harmonic = harmonic + (1/i)
  print(f"{harmonic:.5f}")