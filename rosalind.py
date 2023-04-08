import sys
numbers = []
for i in range (4647, 9328):
    if i % 2 == 1:
        numbers.append(i)
total = sum(numbers)

print(total)
