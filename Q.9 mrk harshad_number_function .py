def harshad_number(a):
    i=a
    rem=0
    b=0
    while a>0:
        rem=a%10
        b=b+rem
        a=a//10
    if i%b==0:
        print("True")
    else:
        print("False")
harshad_number(12)



## till 1 to 100 harshad number:-



i=1
b=[]
while i<=100:
    sum=0
    j=i
    while j>0:
        d=j%10
        sum=sum+d
        j=j//10
    if i%sum==0:
        b.append(i)
    i=i+1
print(b)



