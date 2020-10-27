n=int(input('Enter No:'))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    d=i/fact
    sum=sum+d
print('Sum of Series=',sum)
