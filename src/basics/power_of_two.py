num = int(input("Enter the power: "))
if(num <= 0 or num>31) :
  print("Number should be positive and maximum number is 31")
else: 
  for i in range(num+1) :
    print(f"{2} ^ {i:2d} = {2**i}")