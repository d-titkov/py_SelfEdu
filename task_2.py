# exercise 2.
# The user enters the time in seconds.
# Use string formatting.
total_seconds = int(input("Enter time in seconds: "))

# Convert time to hours, minutes and seconds and output in hh:mm:ss format.
hours = total_seconds // 3600
minutes = total_seconds // 60

# display the result on the screen
print("Time in h:m:s format -", float(hours), ":", float(minutes), ":", total_seconds)