# Problem Statement:
# Simulate a bus seat allocation system with limited seats.
#
# Rules:
# 1. The bus has a total of 40 seats.
# 2. For each booking request:
#    - If requested seats are available → mark as CONFIRMED
#    - If requested seats exceed remaining seats → mark as WAITLISTED
# 3. Update remaining seats after each CONFIRMED booking
#
# Input:
# N             # number of booking requests
# request1      # seats requested in first booking
# request2      # seats requested in second booking
# ...
# requestN      # seats requested in Nth booking
#
# Output:
# CONFIRMED / WAITLISTED   # for each booking in order
#

def bus_seat_allocation(n) :
  max_seats = 40
  while n > 0:
    num_of_bookings = int(input())
    if num_of_bookings <= 0:
      print("Please enter positive integers")
    else:
      if max_seats < num_of_bookings:
        print("WAITLISTED")

      elif max_seats >= num_of_bookings:
        print("CONFIRMED")
        max_seats -= num_of_bookings
    n -= 1

n = int(input())
if n <= 0:
  print("Enter a positive integer")
else:
  bus_seat_allocation(n)