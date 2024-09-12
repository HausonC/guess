import random

r = random.randint(1, 100)
count = 0
while True:
		count += 1 # count = count + 1
		x = input ('please input a int: ')
		x = int (x)
		if x == r:
			print ('you got it')
			print ('this is your', count, 'time guess')
			break
		elif x > r:
			print ('your guess is too big')
		else:
			print ('your guess is too small')
		print ('this is your', count, 'time guess')
	