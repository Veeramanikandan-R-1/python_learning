word=['dog','dog','dog','dog']
string='abcd'
given_pattern='abaa'
result_str=''
word_dic=[]
ind=0
for i in range(len(word)):
	if(word[i] not in word[:i]):
		word_dic.append([word[i],string[ind]])
		result_str+=string[ind]
		ind+=1
	else:
		for word1 in word_dic:
			if(word[i] in word1):
				match=word1[1]
		word_dic.append([word[i],match])
		result_str+=match
if(given_pattern==result_str):
	print("True")
else:
	print("False")
		
print(word_dic)
