import sys

print(sys.maxsize ** 10)

for i in range(0, sys.maxsize ** 10):
	digits = len(str(i))
	number = i
	sum = 0

	for d in range (0, digits):
		sum = (number % 10) ** digits + sum
		number = int(number / 10)

	if (i == sum):
		print(sum)
