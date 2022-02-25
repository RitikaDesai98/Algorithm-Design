#!/usr/bin/env python
# coding: utf-8

# ## Problem 2: Design and implement your own algorithm for Rectangle Multiplication

# In[7]:


# Create a function that takes the 2 numbers that need to be multiplied by rectangle multiplication
# creating a rectangle 
def matrixFormation(number1, number2):

# Use a for loop to iterate over each digit and seperate them. Then mulitply each digit and store their values 
# If the value of multiplication is greater then 10, then store the 10's digit in the upper part else in lower
    diags = [0] * (len(number1) + len(number2))
    for index1, digit1 in enumerate(number1):
        for index2, digit2 in enumerate(number2):
            value = int(digit1) * int(digit2)
            diags[index1+index2+0] += value // 10
            diags[index1+index2+1] += value %  10
            
# Use a for loop to store the values of addition on the diagnol of the matrix, if there is a carry store the floor
# in carry and take the 1's digits into digits. If no carry, store digit directly
    digits = []
    carry   = 0
    for value in reversed(diags):
        value += carry
        if value > 9:
            carry = value // 10
            digits.insert(0, value % 10)
        else:
            carry = 0
            digits.insert(0, value)
            
# If the 1st addition produces a carry store the carry at 1st index
    if carry > 0:
        digits.insert(0, carry)
        
# If the 1st digit is 0, ignore it
    if digits[0] == 0:
        del digits[0]
        
        return digits
    

def rectMultiplication(num1,num2):
    
    f1=0;
    f2=0;
    
    string1 = str(num1)
    string2 = str(num2)
    
    if(string1[0] == "-"):
        string1 = string1.replace('-','')
        f1=1
        
    if(string2[0] == "-"):
        string2 = string2.replace('-','')
        f2=1

    # python calculates:
    
    answer = matrixFormation(string1, string2)
    answer = "%s" % (int(string1) * int(string2))

# Check if number1 &/or number2 is negative, if either are negative add a - sign and print answer else print 
# answer directly
    
    if(f1 != f2):                   
        print("-%s" % (answer))
    
    if(f1==1 and f2==1):
        print("%s" % ( answer))
    
    if(f1==0 and f2==0):
        print("%s" % (answer))
        


# ##### Test Case 1

# In[8]:


rectMultiplication(7000 , 7294)


# ##### Test Case 2

# In[14]:


rectMultiplication(25 , 5038385)


# ##### Test Case 3

# In[15]:


rectMultiplication(-59724 , 783)


# ##### Test Case 4

# In[11]:


rectMultiplication(8516 , -82147953548159344)


# ##### Test Case 5

# In[12]:


rectMultiplication(45952456856498465985 , 98654651986546519856)


# ##### Test Case 6

# In[13]:


rectMultiplication(-45952456856498465985 , -98654651986546519856)

