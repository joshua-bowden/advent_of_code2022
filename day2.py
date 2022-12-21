#!/usr/bin/env python
# coding: utf-8

# In[2]:


#advent of code day 2 - rock paper scissors


# In[4]:


with open('day2_input.txt') as f:
    temp = f.read().splitlines() 


# In[16]:


temp[0]


# In[38]:


#part 1
score = 0

def outcome(a,b):
    global score
    if (a == 'C' and b == 'X') or (a == 'A' and  b == 'Y') or (a == 'B' and b == 'Z'):
        score += 6
    if (a == 'C' and b == 'Z') or (a == 'A' and  b == 'X') or (a == 'B' and b == 'Y'):
        score += 3
    if (a == 'C' and b == 'Y') or (a == 'A' and  b == 'Z') or (a == 'B' and b == 'X'):
        score += 0

def shape(s):
    global score
    if s == 'X':
        score += 1
    if s == 'Y':
        score += 2
    if s == 'Z':
        score += 3
                
score = 0
for x in range(0,len(temp)):
    outcome(temp[x][0], temp[x][2])
    shape(temp[x][2])

print(score)
    


# In[40]:


#part 2
score = 0

def outcome(b):
    global score
    if b == 'Z':
        score += 6
    if b == 'Y':
        score += 3
    if b == 'X':
        score += 0

def shape(s,t):
    global score
    #smarter to go inside first letter to second, than to do first && second like in part 1
    if s == 'A':
        if t == 'X':
            score += 3
        if t == 'Y':
            score += 1
        if t == 'Z':
            score += 2
    if s == 'B':
        if t == 'X':
            score += 1
        if t == 'Y':
            score += 2
        if t == 'Z':
            score += 3
    if s == 'C':
        if t == 'X':
            score += 2
        if t == 'Y':
            score += 3
        if t == 'Z':
            score += 1
                
score = 0
for x in range(0,len(temp)):
    outcome(temp[x][2])
    shape(temp[x][0], temp[x][2])

print(score)

