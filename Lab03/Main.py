seconds = 10000
hours = int(seconds / 3600)
secondsleft = seconds % 3600
seconds = 2800
minutes = int(secondsleft / 60)
remainder = seconds % 60
seconds = 10000123
miliseconds = seconds % 1000


print("Lab03, 100 point version")
print("Starting seconds:", seconds)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remainder)
print("Miliseconds:", miliseconds)