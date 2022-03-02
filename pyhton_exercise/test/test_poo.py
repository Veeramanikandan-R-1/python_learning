'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm"

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:

Input: words = ["omk"]
Output: []
'''

name=['alaska','dad','hello','peace']
#name=['peace']
keyboardlist=['qwertyuiop','asdfghjkl','zxcvbnm']
result=[]
for word in name:
	condition=0
	for word1 in keyboardlist:
		if word[0] in word1:
			for letter in word:
				if letter in word1:
					condition=1
				else:
					condition=0
					break
			print(condition)
			if condition==1:
				result.append(word)
print(result)