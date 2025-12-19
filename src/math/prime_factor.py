num = int(input("Enter number to check prime factor: "))
if(num < 2) :
  print("Number should be 2 or greater")
else:
  i=2
  while(i*i<=num):
    if(num%i == 0):
      print(i, end=" ")
      num = num//i
    else:
      i +=1
  if(num !=0 ):
    print(num)
      