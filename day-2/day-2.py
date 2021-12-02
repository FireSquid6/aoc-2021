# define input class
class movement:
    dir = "^"
    amount = 0


# import and parse the inputs
file = open("day-1\input", "r")
for line in file:
    length = len(line)
