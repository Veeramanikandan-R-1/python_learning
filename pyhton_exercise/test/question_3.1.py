list1=[1,2,3,4,5,6,7]
print("given list:",list1)

print("first 3 elements in a list:",[list1[x] for x in range(3)])
if((len(list1)%2)==0):
	print("middle 3 elements cannot be obtained from the given list")
else:
	half_length=len(list1)//2
	print("middle 3 elements in a list:",[list1[x] for x in range(half_length-1,(half_length+2))])
print("last 3 elements in a list:",[list1[x] for x in range((len(list1)-3),len(list1))])
