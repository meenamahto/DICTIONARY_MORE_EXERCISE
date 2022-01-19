
## in first way:-


list= ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
print(b)



## in second way:-


b=[]
for i in list:
    if i not in b:
        b.append(i)
print(b)

