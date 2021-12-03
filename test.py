import math
import random as rand


# Ask for the input in the following form in order for the
# auto-grader to work correctly
small = float(input("Enter a small decimal number (cm): "))
large = float(input("Enter a large decimal number (cm): "))

radius = rand.randrange(small, large)
area = (radius ** 2) * math.pi

# Output the solution back to the user
print(f"Radius: {radius}cm")
print(f"Volume: {(4 / 3) * (math.pi) * (radius ** 3)}cm^3")
