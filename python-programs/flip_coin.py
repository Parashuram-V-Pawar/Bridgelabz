import random

num = int(input("Enter number of timne to flip coin: "))
head = tail = 0
if(num<0) :
  print("Please enter positive integer")
else:
  for i in range(0, num):
    if(random.random() <= 0.5):
      tail+=1
    else:
      head+=1
  print(f"Heads percentage: {((head*100)/num) :.2f}, Tails percentage: {((tail*100)/num) : .2f} ")
