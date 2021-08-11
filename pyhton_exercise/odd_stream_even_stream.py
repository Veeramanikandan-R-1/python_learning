# condition=input('enter condition')
# limit=int(input('enter limit'))
condition='odd'
limit=5
count=0
if(condition=='odd'):
    i=1
    while(count<limit):
        for j in range(2,i):
            i+=1
            if(i%j==0):
                break
        else:
            print(i)
            count+=1



    # # for k in range(limit):
    # for i in range(limit):
    #     for j in range(2,i):
    #         if(i%j==0):
    #             break
    #     else:
    #         print(i)
if(condition=='even'):
    e=0
    for i in range(limit):
        print(e)
        e+=2


