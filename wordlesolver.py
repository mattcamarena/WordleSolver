import random
# Variables
wordlist = []
green  = [None] * 5
yellow = []
black = []
blackyellow = []
for i in range(5):
	new = []
	blackyellow.append(new)

# import all valid words into wordlist
with open('words.txt', 'r') as file:
	for line in file:
		for word in line.split():
			wordlist.append(word)

def wordle(word, results):
	updateLists(word, results)
	removeWords()
	removeBlackYellows()

# update values
def updateLists(word, results):
	#update lists black(b), yellow(y), green(g)
	for i in range(5):
		if results[i] == 'b':
			if word[i] not in black:
				black.append(word[i])
		elif results[i] == 'y':
			yellow.append(word[i])
			blackyellow[i].append(word[i])
		else:
			green[i] = word[i]

def removeWords():
	for word in wordlist[:]:
		break_out_flag = False
		for i in range(5): # letter by letter check if word is ok
			if(green[i] != None):
				if(green[i] != word[i]):
					wordlist.remove(word)
					break
			elif word[i] in black:
				wordlist.remove(word) 
				break
			else:
				for ch in yellow:
					if(ch not in word):
						wordlist.remove(word)
						break_out_flag = True
						break 
				if(break_out_flag):
					break


def removeBlackYellows():
	for word in wordlist[:]:
		break_out_flag = False
		for i in range(5):
			for j in range(len(blackyellow[i])):
				if(word[i] == blackyellow[i][j]):
					wordlist.remove(word)
					break_out_flag = True
					break 
			if(break_out_flag):
				break
                                                                                                             
x = 5
while(x != 0):
	guess = input("Enter Guess: ")
	results = input("Enter Results black(b), yellow(y), green(g): ")
	wordle(guess, results)
	# print(wordlist[random.randint(0,len(wordlist)-1)])
	print(wordlist)