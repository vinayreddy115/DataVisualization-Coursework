#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
salesMen = ['Ahmed', 'Omar', 'Ali', 'Ziad', 'Salwa', 'Lila']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]


# In[2]:


df = pd.DataFrame()
df ['Name'] =salesMen
df ['Mobile_Sales'] = Mobile_Sales
df['TV_Sales']=TV_Sales


# In[3]:


df.set_index("Name",drop=True,inplace=True)


# In[4]:


df


# ## A. Create a bar plot of the sales volume.

# In[6]:


df.plot.bar( figsize=(20, 10), rot=0).legend(bbox_to_anchor=(1.1, 1)) 
plt.xlabel('Salesmen') 
plt.ylabel('Sales')
plt.title('Sales Volume for two salesmen in \nJanuary and April 2017')
plt.show()


# ### B. Create a pie chart of item sales.
# 

# In[7]:


df.plot.pie(subplots=True)


# ## C. Create a box plot of item sales.

# In[8]:


df.plot.box()


# ## D. Create an area plot of item sales.
# 

# In[9]:


df.plot.area(figsize=(6, 4)).legend(bbox_to_anchor=(1.3,1))


# ## E. Create a stacked bar plot of item sales.
# 

# In[11]:


df.plot.bar(stacked=True, figsize=(20, 10)).legend
bbox_to_anchor=(1.1, 1)


# In[ ]:




