def fizz(x):
	output = [];

	for i in range(1, x + 1):
		if i % 3 == 0:
			array.append("Fizz");

		elif i % 5 == 0:
			array.append("Buzz");

		else:
			array.append(str(i));

	return array;
