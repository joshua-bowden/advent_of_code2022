#!/usr/bin/env python
# coding: utf-8

# In[1]:


#advent of code day 3 - rucksack


# In[3]:


with open('day3_input.txt') as f:
    temp = f.read().splitlines() 


# In[48]:


#part 1
#  uh oh, debug comments getting left in now

prioSum = 0
for x in range(len(temp)):
    for letter in temp[x]:
        
        index = -1
        index = temp[x].find(letter, int(len(temp[x])/2))
        if index > -1:
            #print (temp[x][index])
            break
    if temp[x][index].islower():
        #print (ord(temp[x][index]) - 96)
        prioSum += (ord(temp[x][index]) - 96)
    else:
        #print (ord(temp[x][index]) - 38)
        prioSum += (ord(temp[x][index]) - 38)
        
print (prioSum)


# In[51]:


#part 2

prioSum = 0
for x in range(0, len(temp), 3):
        
    for letter in temp[x]:
        index1 = -1
        index2 = -1
        index1 = temp[x+1].find(letter)
        index2 = temp[x+2].find(letter)
        if index1 > -1 and index2 > -1:
            break
    #temp[x+1][index1] and temp[x+2][index2] should be same
    if temp[x+1][index1].islower():
        prioSum += (ord(temp[x+1][index1]) - 96)
    else:
        prioSum += (ord(temp[x+1][index1]) - 38)
        
print (prioSum)

