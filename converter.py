import random
import time

n = random.randint(0, 50)

correct = True
while correct == True:
	correct = False
	print("What is 2 ** {}?".format(n))

	r = n % 10
	d = n // 10

	answer = 2**r
	if d == 1:
		answer = str(answer) + 'K'
	elif d == 2:
		answer = str(answer) + 'M'
	elif d == 3:
		answer = str(answer) + 'B'
	elif d == 0:
		answer = str(answer) + ""
	else:
		answer = str(answer) + 'T'
	print(answer)

	a = input()
	if a != answer:
		print("Wrong, try again")
		correct = True
	else:
		collect = False

#"What is 2 ** 10?
#answer = 1k
