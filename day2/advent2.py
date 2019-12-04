desired_goal = 19690720

def complete_process():
	for noun in range(0, 100):
		for verb in range(0, 100):
			input = [int(x) for x in "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,2,27,10,31,1,5,31,35,2,35,6,39,1,6,39,43,2,13,43,47,2,9,47,51,1,6,51,55,1,55,9,59,2,6,59,63,1,5,63,67,2,67,13,71,1,9,71,75,1,75,9,79,2,79,10,83,1,6,83,87,1,5,87,91,1,6,91,95,1,95,13,99,1,10,99,103,2,6,103,107,1,107,5,111,1,111,13,115,1,115,13,119,1,13,119,123,2,123,13,127,1,127,6,131,1,131,9,135,1,5,135,139,2,139,6,143,2,6,143,147,1,5,147,151,1,151,2,155,1,9,155,0,99,2,14,0,0".split(',')]
			total_inputs = len(input)
			input[1] = noun
			current_position = 0
			input[2] = verb
			for i in range(0, total_inputs):
				if input[0] == desired_goal:
					print(noun)
					print(verb)
					return
				input_1 = input[current_position + 1]
				input_2 = input[current_position + 2]
				if input[current_position] == 1:
					output = input[input_1] + input[input_2]
				elif input[current_position] == 2:
					output = input[input_1] * input[input_2]
				elif input[current_position] == 99:
					break
				input[input[current_position + 3]] = output
				current_position += 4

complete_process()
	