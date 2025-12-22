# Problem Statement: 2D Array
#
# Description:
# Create a program/library that reads a 2D array of integers, floats (doubles),
# or booleans from standard input and prints the array to standard output.
#
# Input:
# - M → number of rows
# - N → number of columns
# - M × N values → elements of the 2D array entered row-wise
#   (In Java, Scanner is used for input; in Python, input() is used)
#
# Output:
# - Print the 2D array to standard output
# - Each row should be printed on a new line with elements separated by spaces
#   (In Java, PrintWriter with OutputStreamWriter is used; in Python, print statements are used)

def two_d_array(row, col):
  datatype = int(input("Choose data type to store:\n1. integer\n2. Float\n3. Boolean\n"))
  if datatype == 1:
    a = [[int(x) for x in input().split()] for _ in range(row)]
    print(a)
  elif datatype == 2:
    a = [[float(x) for x in input().split()] for _ in range(row)]
    print(a)
  elif datatype == 3:
    print("Enter values for boolean in 1's or 0's")
    a = [[bool(int(x)) for x in input().split()] for _ in range(row)]
    print(a)

row = int(input())
col = int(input())
if row < 0 or col <0 :
  print("rows and columns value cannot be a negative integer.")
else:
  two_d_array(row, col)
