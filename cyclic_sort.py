#Implementation of cyclic sort in python

mylist=[6,4,2,3,5,1]

for index in range(len(mylist)):
    while mylist[index] != index+1:
        correct_index=mylist[index]-1
        mylist[index],mylist[correct_index]=mylist[correct_index],mylist[index]
print(mylist)
