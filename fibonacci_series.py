#num=int(input("enter number"))
prev=0
cur=1
sum=0
print(prev)
print(cur)
while(sum<=50) :
    temp=cur
    cur=prev+cur
    prev=temp
    print(cur)
    sum+=prev 