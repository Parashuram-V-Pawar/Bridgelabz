# Problem Statement:
# Simulate mobile battery drain based on app usage.
#
# - The battery starts at 100%.
# - Each app drains a fixed percentage per minute (drain_per_minute).
# - The simulation stops when battery level becomes less than or equal to 0.
# - Print the total number of minutes the battery lasted.
#
# Input:
# drain_per_minute   # integer or float, percentage drained per minute
#
# Output:
# minutes           # total minutes before battery reaches 0 or below
#
# Function to calculate number of minutes mobile runs
def mobile_battery_drain_simulator(drain_per_minute):
  minutes = 0
  battery = 100
  # Till battery gets 0 loop runs
  # Every time loop is executed minutes is incremented by 1 and battery is decremented by drain_per_minute
  while battery > 0:
    minutes += 1
    battery -= drain_per_minute
  # When loop condition fails minutes is returned
  return minutes

# Input statement, expecting float input to also calculate when float value is input
drain_per_minute = float(input("Enter drain per minute: "))
# Calling the mobile_battery_drain_simulator function and printing the returned value
print(mobile_battery_drain_simulator(drain_per_minute))
