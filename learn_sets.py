# Enter your code here. Read input from STDIN. Print output to STDOUT
m=raw_input("\n")
set1=raw_input("\n")
#print set1
list1=set1.split()
#print list1
list1=list(map(int,list1))
print list1
n=raw_input("\n")
set2=raw_input("\n")
#print set2
list2=set2.split()
#print list2
list2=list(map(int,list2))
#print list2
ll1=len(list1)
#print("length of list1 %s" %ll1)

ll2=len(list2)
#print("length of list2 %s" %ll2)
list3=[]
flag =1

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j] :
            flag=0
            continue
    if flag==1:
        list3.append(list1[i])
#        print list3
    flag=1
for i in range(len(list2)):
    for j in range(len(list1)):
        if list2[i]==list1[j]:
            flag=0
            continue
    if flag==1:
        list3.append(list2[i])
    flag=1
list4=map(int,list3)
for i in range(len(list4)):
    print list4[i]








