list = [1,2,3,4,5,6]
rotate_times=int(input())
new_list=[]
new_list.extend(list[rotate_times:])
new_list.extend(list[:rotate_times])
print(new_list)