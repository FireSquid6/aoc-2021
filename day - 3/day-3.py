# define and import functions
import math


def sign(n):  # returns 1 if the number is positive, and -1 if the number is negative
    if abs(n) == n:
        return 1
    else:
        return -1


def bin_to_decimal(bitstring):
    n = 0
    i = len(bitstring)
    bit = 0

    while i > 0:
        n += int(bitstring[i]) * (2 ** bit)

        i -= 1
        bit += 1

    return n


# open the file
file = open("day - 3\input.txt", "r")
bit_amounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# parse the input
for line in file:  # for each line in the input file
    for i in range(0, len(line) - 1):  # for each character in the current line
        # get n
        if line[i] == "0":
            n = -1
        else:
            n = 1

        # add n to the bit amounts array
        bit_amounts[i] += n

# get the gamma and epsilon rate
bin_gamma_rate = ""
bin_epsilon_rate = ""

for i in range(0, len(bit_amounts) - 1):
    if bit_amounts[i] < 0:
        bin_gamma_rate += "0"
        bin_epsilon_rate += "1"
    else:
        bin_gamma_rate += "1"
        bin_epsilon_rate += "0"

# convert the binary numbers into decimal
dec_gamma_rate = bin_to_decimal(bin_gamma_rate)
dec_epsilon_rate = bin_to_decimal(bin_epsilon_rate)

# print the output
print(str(dec_gamma_rate * dec_epsilon_rate))
