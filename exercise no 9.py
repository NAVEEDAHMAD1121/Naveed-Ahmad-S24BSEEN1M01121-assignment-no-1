list1=[3,6,5,4,3,2,6]
list2=[4,4,3,4,5,7,3]
new_list=[i for i in list1 if i % 2 !=0]+[j for j in list2 if j % 2 ==0]
print(new_list)