#!/usr/bin/env python
# coding: utf-8

# ### lambda function

# In[ ]:


greet = lambda name : print(f"Good Morning {name}")
greet("varun")


# In[ ]:


a = int(input())
b = int(input())
c = int(input())
product = lambda a,b,c : a*b*c
product(a,b,c)


# In[ ]:


even = lambda L : [x for x in L if x %2 == 0]
my_list = [100,202,30,5,25,0,2]
even(my_list)

