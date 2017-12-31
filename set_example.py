# Enter your code here. Read input from STDIN. Print output to STDOUT
m=raw_input()
set1=raw_input()
#print set1
list1=set1.split()
#print list1
list1=set(map(int,list1))
#print list1
n=raw_input()
set2=raw_input()
#print set2
list2=set2.split()
#print list2
list2=set(map(int,list2))
list3=list2.difference(list1)
list3=list(map(int,list3))
print list3
list5=list1.difference(list2)
list5=list(map(int,list5))
print list5

#list6=list6.append(list5)
for j in range(len(list5)):
    print list5[j]
for i in range(len(list3)):
    print list3[i]









