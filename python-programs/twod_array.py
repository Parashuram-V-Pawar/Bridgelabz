rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

arr = []
print("Enter the elements row wise: ")
for i in range(rows):
  row = list(map(int, input().split()))
  arr.append(row)

print("The 2D array elements are: ")
for i in range(rows):
  for j in range(columns):
    print(arr[i][j], end=" ")
  print()
    