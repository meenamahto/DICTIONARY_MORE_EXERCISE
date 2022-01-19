list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new_list=[]
for i in list1:
    for j in list2:
        if i==j:
            new_list.append(i)
print(new_list)



## in second way

i=0
c=[]
while i<len(list1):
    j=0
    b=0
    while j<len(list2):
        if list1[i]==list2[j]:
            b=list1[i]
        j=j+1
    i=i+1
    c.append(b)

print(c)




