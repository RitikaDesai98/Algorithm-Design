#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Design and implement your own algorithm that takes the array A with size m+n and merges the two subarrays using an auxiliary array Aux of size min {m, n} back into array A sorted in ascending order.

# In[6]:


# Create a function that takes the number of elements in an array and sorts the 2 sorted subarrays a[m+n]
# into a single sorted array using a aux[min{m,n}]

def arraySort(n):
    a = []
    aux = []
    
# Give input values of the array a[m+n]
    for i in range(0,n):
        x =int(input())
        a.append(x)
        
# Use a flag value to test the three cases of sorting, i.e., m>n, m=n, m<n
    f=0;
    
# Use a for loop to find the seperation point of the subarrays i.e., where a[m] ends and where a[n] starts 
# and set the f variable to 1,2,3 to further include conditions for each case
    for i in range(1,n):              
        if a[i] < a[i-1]:            
            if(i > (n//2)):           
                f=1;
                t=i                
                break;
            if(i == (n/2)):
                f=2; 
                t=i
                break;
            else:
                f=3
                t=i                
                break;
                
# Take a[n] out of a[m+n] and store it in aux[n] as a[n] is smaller
    if(f==1):
        for i in range(t,n):         
            aux.append(a[i])
            a.remove(a[i])
            
# Take a[m] out of a[m+n] and storing it in aux. In this case, the size of a[m] & a[n] is the same so we
# can take out any of them
    elif(f==2):
        for i  in range(0,t):
            aux.append(a[0])
            a.remove(a[0])

# Take a[m] out of a[m+n] and storing it in aux as a[m] is smaller
    elif(f==3):
        for i in range(0,t):
            aux.append(a[0]) 
            a.remove(a[0]) 
            
# If either of a[m] or a[n] is null, return the input array
    elif(f==0):
        return(a)
    
# Use a for loop to finally sort a & aux and sort the sorted array into a and print it
    for j in range(0,n):
        if(aux[0] < a[j] or aux[0]==a[j]):       
            a.insert(j,aux[0])
            aux.remove(aux[0])
            if(len(aux)==0):
                break;
    return(a)
        


# ##### Test Case 1

# In[7]:


arraySort(3)


# ##### Test Case 2

# In[8]:


arraySort(4)


# ##### Test Case 3

# In[9]:


arraySort(8)


# ##### Test Case 4

# In[10]:


arraySort(19)

