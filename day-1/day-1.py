# import
file = open("day-1\input", "r")

# convert
data_list = []
for line in file:
    data_list.append(int(line))

# iterate through the list
length = len(data_list)
increased = 0
decreased = 0
i = 1
while i < length:
    if data_list[i] > data_list[i - 1]:
        increased += 1
    else:
        decreased += 1
    i += 1

# print the outputs
print(f"The data increases {increased} times.")
print(f"The data decreases {decreased} times.")
