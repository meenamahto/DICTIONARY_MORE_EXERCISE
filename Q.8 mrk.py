# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# new_list=[]
# for i in list1:
#     for j in list2:
#         if j not in new_list :
#             new_list.append(j)
#         elif  i not in new_list:
#             new_list.append(i)
# print(new_list)
        

# l=["one",'two','three',"four","five"]
# d={}
# for i in range(5):
#     n=int(input("Enter your number:"))
#     d.update({n:l[i]})
# print(d)


# d={"c1":[1,2,3],"c2":[5,6,7],'c3':[9,10,11]}
# c1,c2,c3=d.values()
# print("c1","c2","c3")
# i=0
# while i<len(c1):
#     j=0
#     while j<len(c2):
#         k=0
#         while k<len(c3):
#             if i==j and j==k:
#                 print(c1[i],c2[j],c3[k])
#             k=k+1
#         j=j+1
#     i=i+1



# a={1:10,2:20,3:30,4:40,5:50,6:60}
# print("key" ,"values","count")
# count=0
# for i in a:
#     count+=1
#     print(i,a[i],count)
 


a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
d={}
# e={}
for i in range(len(b)):
    e={}
    for j in range(len(c)):
        e.update({b[i]:c[i]})
    d.update(e)
print(d)
