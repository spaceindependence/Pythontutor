minutesFromTheStartOfTheDay = int(input())
hours = (minutesFromTheStartOfTheDay % 1440) // 60
minutes = (minutesFromTheStartOfTheDay %1440) % 60
print(hours)
print(minutes)