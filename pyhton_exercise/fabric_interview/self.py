words=int(input("enter a number of words\n"))
words_list=[]
for i range(words):
	word=str(input())
	words_list.append(word)
for i in words_list:
	if((words_list.count(i)>1) and (i not in words_list[:(words_list)]):
		print(words_list.count(i))