#!/usr/bin/env python
# coding: utf-8

# ## Problem 2: Design and implement your own algorithm for Ala Carte Multiplication

# In[8]:


# Create a funtion that takes input of 2 numbers to multiply it by the Ala Carte Multiplication method

def acMultiplication(number1, number2):
    posNum1 = abs(number1)
    posNum2 = abs(number2)

    answer = 0

    a1=0
    a2=0
    
# First check if either of the input numbers are negative numbers and respectively set a1 or a2 to 1
    if(number1 <0):
        a1=1

    if(number2 <0):
        a2=1
        
# As we divide 1st number by 2 everytime, we quit the loop once the number is less than 1
    while(posNum1 > 0):
        # If the 1st number's last digit is odd, we add the corresponding 2nd number to the answer
        if(posNum1 % 2==1):

            answer = answer + posNum2;

# The 1st number gets divided by 2 and 2nd number gets multiplied by 2
        posNum2 = posNum2*2

        posNum1 = posNum1//2;

# Check the a1 and a2 values, if positive we directly print the answer else if either one is negative
# add a negative sign and if both are negative then directly print the answer

    if(a1==1 and a2==1):   

        print(answer)

    if(a1==0 and a2==0):

        print(answer)

    if(a1 != a2):

        print('-',answer)


# #### Test Case 1

# In[9]:


acMultiplication(7000 , 7294)


# #### Test Case 2

# In[10]:


acMultiplication(25 , 5038385)


# #### Test Case 3

# In[11]:


acMultiplication(-59724 , 783)


# #### Test Case 4

# In[12]:


acMultiplication(8516 , -82147953548159344)


# #### Test Case 5

# In[13]:


acMultiplication(45952456856498465985 , 98654651986546519856)


# #### Test Case 6

# In[14]:


acMultiplication(-45952456856498465985 , -98654651986546519856)

