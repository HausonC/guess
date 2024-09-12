import random

start = input ('please set a start no.: ')
end = input ('please set a end no.: ')
start = int (start)
end = int (end)

r = random.randint(start, end)
count = 0
while True:
		count += 1 # count = count + 1
		x = input ('please guess a number: ')
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
	