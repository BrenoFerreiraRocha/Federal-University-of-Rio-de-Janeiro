def program():
	firstInput = raw_input("")
	counter = 0;
	while(int(counter) < int(firstInput)):
		counter += 1
		pairNumbers = ""
		number1 = 0;
		number2 = 0;
		pairNumbers = raw_input("")
		number1 = int(pairNumbers.partition(',')[0])
		number2 = int(pairNumbers.partition(',')[2])
		print(str(number1))
		print(str(number2))
		while(number2 != 0):
			resto = number1 % number2
			number1 = number2
			number2 = resto
			print(str(number2))
			if(number2 == 0):
				print("---")
program()

