import pandas as pd


df = (pd.read_excel (r'C:\Users\R.Mohan Raj\Documents\institute_data.xlsx'))
# print(df)
# print(len(df))
# for i in list(df):
#     print(i)
mylist = df['data'].tolist()
print(len(mylist))
distinct=[]
for i in range(len(mylist)-1):
    if(mylist[i]!=mylist[i+1]):
        distinct.append(mylist[i])
    else:
        continue
#
distinct_1=[]
for i in range(len(distinct)):
    if((distinct[i] not in distinct[:i])):
        distinct_1.append(distinct[i])

print(len(distinct_1))
#
for i in distinct_1:
    print(i)

# list=[1,2,34,5]
# print(list[2:])
