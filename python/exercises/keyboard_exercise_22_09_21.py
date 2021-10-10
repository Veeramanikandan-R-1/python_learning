keyboard_list=["qwertyuiop","asdfghjkl","zxcvbnm"]
words=["Hello","Alaska","Dad","Peace"]
#words=["omk"]
result_list=[]
for word in words:
	print(word)
	for row in keyboard_list:
		print(row)
		count=0
		for letter in word:
			if(letter.lower() not in row):
				continue
			else:
				print(letter)
				count+=1
		if(count==len(word)):
			result_list.append(word)
		else:
			continue				
print(result_list)
