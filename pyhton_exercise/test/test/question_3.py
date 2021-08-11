# question
# from the given list find i)first 3 elements in a list
# ii)find middle 3 elements in a list
# iii)find last 3 elements in a list

# answer
list1=[1,2,3,4,5,6,7]
list_len=len(list1)
print("given list:",list1)
print("first 3 elements in a list:",list1[:3])

if((len(list1)%2)==0):
	print("middle 3 elements cannot be obtained from the given list")
else:
	half_length=list_len//2
	print("middle 3 elements in a list:",list1[half_length-1:(half_length+2)])

print("last 3 elements in a list:",list1[(list_len-3):])
