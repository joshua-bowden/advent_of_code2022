#!/usr/bin/env python
# coding: utf-8

# In[2]:


#advent of code day 1 - calories elves


# In[3]:


with open('day1_input.txt') as f:
    temp = f.read().splitlines()    


# In[4]:


#part 1

pastSum = 0
currentSum = 0
for x in range(len(temp)):
    if temp[x] != "":
        currentSum  += int(temp[x])
    else: 
        pastSum = max(pastSum, currentSum)
        currentSum = 0
#pastSum is greatest collection of unbroken lines = elf with most calories
pastSum


# In[15]:


#part 2
top1 = 0
top2 = 0
top3 = 0
currentSum = 0
for x in range(len(temp)):
    if temp[x] != "":
        currentSum  += int(temp[x])
    else:
        if currentSum > top1:
            #shuffle down
            top3 = top2
            top2 = top1
            top1 = currentSum
            currentSum = 0 
        elif currentSum > top2:
            top3 = top2
            top2 = currentSum
            currentSum = 0
        elif currentSum > top3:
            top3 = currentSum
            currentSum = 0
        else:
            currentSum = 0

print(top1+top2+top3)

