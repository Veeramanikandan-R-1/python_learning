strs = ["eat","tea","tan","ate","nat","bat"]
#strs=['a']
result=[]
common=[]
index=-1
for word_index in range(len(strs)-1,0,-1):
	temp=[]
	for word in strs[:index]:
		count=0
		for letter in strs[word_index]:
			if(letter in word):
				count+=1		
		if(count==len(word)):
			if word not in common:
				temp.append(word)
			common.append(word)
	if(count<len(strs[word_index]) and (strs[word_index] not in result)):
		if strs[word_index] not in common:
			temp.append(strs[word_index])
	if(len(temp)>0):
		result.append(temp)
	index-=1
print(result)
			
	
	
