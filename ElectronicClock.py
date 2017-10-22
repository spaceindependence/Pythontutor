n = int(input())
hours = (n % 1440) // 60
minutes = (n % 1440) % 60
print(hours)
print(minutes)
