#!/usr/bin/env python3

#Total of 162 words, listing the hedge words from the sentence
from colorama import Fore, Style

'''			Issues are listed below
1.) There needs to be a way to determine the hedge words even with different symbols 
that are present

2.) Case-Sensitive

'''
#Loading Hedge words
def loadHedge():
	pull_data = open("hedgeWords.txt","r")
	hedgeWords = pull_data.readlines()
	pull_data.close()
	return hedgeWords

hedgeWords = loadHedge()

#Loading the user's sentence
user_input = input("Enter sentence: ")
print(10 * '\n')
#Checking if any are a hedge word
user_sentence = []

#function to split up code
def split_line(text):
    # split the text
    words = text.split()
    return words

#saving the variables into a array
user_sentence = split_line(user_input)
length_sentence = (len(user_sentence))


hedgeWords = list(map(str.strip, hedgeWords))
values = []
length_hedgeWrods = len(hedgeWords)
print(Fore.WHITE + 'Input Sentence: ' + user_input)
print('\nHedge Words listed below: ')
for x in range(0,length_sentence):
	
	for y in range(0,length_hedgeWrods):
		if user_sentence[x] == hedgeWords[y]:
			#Saving the locations of hedge words
			values.append(user_sentence[x])
			print(Fore.BLUE + user_sentence[x])
			#print(Fore.GREEN, values)


print(Fore.WHITE + '\nHedged Output: ')
for w in user_input.split():
   if w in values:
    	print(Fore.RED+w, end=" ")
   else:
    	print(Fore.WHITE+w, end= " ")

    	
print(Fore.GREEN + '\nFinished, Press Up-Key once and then Press "Enter" to try another sentence.. ')
		