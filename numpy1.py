import numpy as np

# arr=np.array((1,2,3,4,5))
# print(arr[0])
# c= arr*2
# print(c)
# print(arr[1]+arr[3])

# l=([[1,2,3],[4,5,6]])
# for k in l:
#     for i in k:
#         print(i * 2, end= " ")

# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[1,4])

# arr=np.array([[1,2],
#             [3,4]])
# arr2=np.array([[1,2,3,4,5,6,7,8]])
# arr=np.array([1,2,3,4], ndmin=5)
# print(arr2[0][2:5])
# print(arr2.shape)
# print(arr)


# l=[1,2,3,4,5,6,7]
# print(l[1:5])

# l=[[1,2,3,4,5],[6,7,8,9,10]]
# l=[1,2,3,4,5]
# l.append(6)
# print(l)

arr=np.array([1,2,3])
arr=np.append(arr,4)
# arr=np.insert(arr,2,10)
# print(arr)

arr=np.insert(arr, 2, [10,20],axis=0)
print(arr)

# print(l[1,4])
# print((l[0][0], l[0][1], l[0][2], l[0][3], l[0][4]) (l[1][0], l[1][1], l[1][2], l[1][3], l[1][4]))


# c=arr*2
# print(c)
# print(arr[1,4])


# arr=np.array([1,2,3,4,5,6,7,8,9])
# newarr=arr.reshape(3,1,3)
# print(newarr)

# for i in arr:
#     print(i)

# for k in newarr:
#     for l in k:
#         for m in l:
#             print(m)

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.concatenate((arr1,arr2))
# print(arr)

# arr3=np.array([[1,2]])
# arr4=np.array([[3,4]])
# arr5=np.array([[6,7]])
# arrr=np.concatenate((arr3,arr4,arr5), axis=1)
# print(arrr)
# print(arrr.shape)

# arr1=np.array([1,2,3])
# arr2=np.array([3,4,5])
# arrr=np.stack((arr1, arr2), axis=1)
# print(arrr)

# arr1=np.array([1,2,3])
# arr2=np.array([3,4,5])
# arraye=np.hstack((arr1, arr2))
# print(arraye)

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.vstack((arr1, arr2))
# print(arr)

# arr1=np.array([1,2,3])
# arr2=np.array([3,4,5])
# arrr=np.dstack((arr1, arr2))
# print(arrr)

# arr=np.array([1,2,3,4,5,6])
# newarr=np.array_split(arr, 10)
# print(newarr)
# print(newarr[0].shape)

# arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# newarr=np.array_split(arr,4)
# print(newarr[0].shape)
# print(newarr)

# arr=np.array([1,2,3,4,5,4,4])
# x=np.where(arr==1)
# print(x)

# arr=np.array([[3,2,4],[5,0,1]])
# print(np.sort(arr))

# arr=np.array([1,2,3,4,5,6,7])
# filter_arr=[]
# for element in arr:
#     if element % 2 == 0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# print(filter_arr)
# new_arr=arr[filter_arr]
# print(new_arr)