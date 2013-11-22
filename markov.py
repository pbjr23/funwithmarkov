import random

def parse(filename):
	f = open(filename)
	readFile = f.read()

	readFile = readFile.split()

	markovpairs = {}
	for i in range(len(readFile)-2):
		markovpairs.setdefault((readFile[i],readFile[i+1]), []).append(readFile[i+2])

	return markovpairs

def printer(filename, words):
	markovpairs = parse(filename)
	init = random.choice(list(markovpairs.keys()))
	acc = " ".join(init)

	for i in range(words):
		next = random.choice(markovpairs[init])
		acc += " " + next
		init = (init[1], next)

	print(acc)

printer("bible.txt", 30)