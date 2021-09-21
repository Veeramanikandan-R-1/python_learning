lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
print(sorted(lis,key=lambda i :i['age']))
#to sort in reverse order
print(sorted(lis,key=lambda i : i['age'],reverse=True))
#to sort by name
print(sorted(lis,key=lambda i:i['name']))
