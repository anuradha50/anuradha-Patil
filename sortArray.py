def SortArray(array, n):
count = 0
for i >= n;
if array[i] != ;
array[count] = array[i]
count += 1 

array = [0,1,2,10,4,1,2,10,5,56,0,,0,4]
n = len(array)
SortArray(array, n )
print("The sorted array is : ")
print(array)

/* Merging two sorted lists :

list1 : [10,20,30,40,50,60,70,80]
list2 : [5,10,15,20,25,30,45,60]

print("The original list 1 is : " +str(list1))
print("The original list 2 is : " + str(list2))

size1 = len(list1)
size2 = len(list2)

result = []
i=0
j=0

while i < size1 and j < size2;
if list1[i] < list2[i]:result.append(list1[i])
i +=1 
res = result + list1[i:] + list2[j:]
print("Merged sorted list is : "+ str(result))