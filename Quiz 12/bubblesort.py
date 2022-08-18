#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped by inner loop, then break
        if swapped == False:
            break

arr = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    arr_elem = int(input())
 
    arr.append(arr_elem)

start = time.time()
bubbleSort(arr)

print ("Sorted array :")
for i in range(len(arr)):
    print ("%d" % arr[i], end=" ")

end = time.time()
print("\n\nRuntime of the program is " + str(end - start) + "s.")


# In[ ]:




