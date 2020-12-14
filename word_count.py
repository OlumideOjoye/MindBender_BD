from collections import Counter

file = open("/home/olumide/Documents/Shakespeare.txt", "rt")

def word_count():
	data = file.read()
	for char in '"''!@#$%^&*()-_=+,<.>/?;:[{]}~`\|':
		data = data.replace(char, ' ')
	data = data.lower()
	words = data.split()
	print('Number of words in text file :', len(words))

word_count()
