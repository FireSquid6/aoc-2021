import input
import statistics as stats

# get the mean
m = stats.mean(input.list)
m = round(m)
print(str(m))

# calculate the total amount of fuel
fuel = 0
for n in input.list:
    steps = abs(n - m)
    i = 1
    cost = 0

    while i <= steps:
        cost += i
        i += 1

    fuel += cost

# print the amount of fuel
print(str(fuel))
