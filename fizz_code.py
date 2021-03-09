def fizz(x):
	output = [];

	for i in range(1, x + 1):
		if i % 3 == 0:
			output.append("Fizz");

		elif i % 5 == 0:
			output.append("Buzz");

		else:
			output.append(str(i));

	return output;
