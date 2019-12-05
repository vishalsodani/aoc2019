met_criteria = 0
for input in range(382345, 843167):
	input = str(input)
	previous_digit = -1
	adjacent_rule_passed = False
	increase_rule_passed = False
	for digit in input:
		if adjacent_rule_passed == False and previous_digit != -1 and int(digit) == previous_digit:
			adjacent_rule_passed = True
			
		if previous_digit != -1:
			if int(digit) >= int(previous_digit):
				increase_rule_passed = True
			else:
				increase_rule_passed = False
				break
		
		previous_digit = int(digit)
	
	if adjacent_rule_passed and increase_rule_passed:
		met_criteria += 1
	
print(met_criteria)
		