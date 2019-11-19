#!/usr/bin/env python
# coding: utf-8

# In[6]:


with open('dataset_3363_2.txt') as f:
    s=f.readline()


# In[7]:


print(s)


# In[9]:


l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
 

j=0
for i in s:
    
    if i.isalpha():
        g=i*integ[j]
        print(g)
        #r.append(g)
        j+=1
#print (*r, '')


# In[ ]:




