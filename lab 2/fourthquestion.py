print("please enter a number: ")
number = input()
number = int(number)
i = 0
for value in range(2, number//2 + 1):
	if number%value == 0:
		i+=1
		print("its not a prime number")
		break
if i == 0:
	print("its a prime number")