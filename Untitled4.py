#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv(r'C:\Users\Lakshmi\Match.csv')


# In[2]:


data


# # Print no. of matches won by each team based on year wise (each year as one column)

# In[27]:


df = pd.DataFrame(data.groupby(['Season_Year','match_winner'])['match_winner'].count())


# In[28]:


df


# # Print  ManOfMach count of each player in  Hyderabad stadium
# 
# 

# In[22]:


x=data[data.City_Name=='Hyderabad']
x.ManOfMach.count()


# In[23]:


y=x.ManOfMach.value_counts()
y


# #  Print number of matches won and loss(as two columns). Consider as win when a team wins Toss  and Match . print for each and every team
# 
# 

# In[ ]:





# In[ ]:




