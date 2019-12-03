total = 0
with open('input.txt') as fp:
	for input in fp:
		total += (int(input) / 3) - 2
		next_input = (int(input) / 3) - 2
		while next_input > 0:
			next_input = (next_input / 3) - 2
			if next_input > 0:
				total += next_input
print(total)