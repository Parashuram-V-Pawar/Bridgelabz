def two_d_array_input(rows, columns, datatype):
  arr = []

  #input statement
  print("Enter the elements row wise: ")
  for i in range(rows):
    l = list(map(datatype, input().split()))
    arr.append(l)

  #print statement
  print("The 2D array elements are: ")
  for i in range(rows):
    for j in range(columns):
      print(arr[i][j], end=" ")
    print()





rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

datatype = input("Enter the type of data you want to store (int/float/boolean): ").lower()
if(datatype == 'int'):
  two_d_array_input(rows, columns, int)
elif(datatype == 'float'):
  two_d_array_input(rows, columns, float)
elif(datatype == 'boolean'):
  if datatype in ("true","t","1","yes","y"):
    boolean_val = True
  elif datatype in ("false","f","0","no","n"):
    boolean_val = False 
  two_d_array_input(rows, columns, boolean_val)
else:
  print("Invalid data type selected.")