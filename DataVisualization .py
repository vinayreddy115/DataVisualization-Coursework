#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


plt.style.use('seaborn-whitegrid')
X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]


# In[3]:


plt.scatter(X,Y)
plt.xlim(0,1000)
plt.ylim(0,100)


# In[4]:


#scatter plot color
plt.scatter(X, Y, s=60, c='red', marker='^')


# In[5]:


#change axes ranges
plt.xlim(0,1000)
plt.ylim(0,100)


# In[6]:


#add title
plt.title('Relationship Between Temperature and Iced Coffee Sales')


# In[7]:


plt.xlabel('Sold Coffee')
plt.ylabel('Temperature in Fahrenheit')


# In[8]:


#show plot
plt.show()


# ## Visualizing data using Matplotlib

# In[9]:


plt.style.use('seaborn-whitegrid')
# Create empty figure
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)


# In[10]:


ax.plot(x, np.sin(x));
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))


# In[11]:


plt.xlim(0, 11)
plt.ylim(-2, 2)
plt.axis('tight')


# In[12]:


#add title
plt.title('Plotting data using sin and cos')


# ## Importing and Using the Seaborn Library

# In[13]:


import seaborn as sns


# In[14]:


plt.style.use('classic')
plt.style.use('seaborn-whitegrid')


# In[15]:


# Create some data
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]],
size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])


# In[16]:


# Plot the data with seaborn
sns.distplot(data['x'])
sns.distplot(data['y']);


# In[17]:


for col in 'xy':
 sns.kdeplot(data[col], shade=True)


# In[18]:


sns.kdeplot(data);


# In[19]:


with sns.axes_style('white'):
 sns.jointplot("x", "y", data, kind='kde');


# In[20]:


with sns.axes_style('white'):
 sns.jointplot("x", "y", data, kind='hex')


# In[21]:


sns.pairplot(data)


# ## Importing and Using the Plotly Library

# In[22]:


pip install plotly==4.5.4


# In[80]:


import plotly
from plotly.offline import iplot
import plotly.graph_objs as go


# In[81]:


x = np.random.randn(2000)
y = np.random.randn(2000)


# In[82]:


iplot([go.Histogram2dContour(x=x, y=y,
contours=dict (coloring='heatmap')),
go.Scatter(x=x, y=y, mode='markers',
marker=dict(color='white', size=3,
opacity=0.3))], show_link=False)


# In[46]:


import plotly.offline as offline
import plotly.graph_objs as go
offline.plot({'data': [{'y': [14, 22, 30,
44]}],'layout': {'title': 'Offline Plotly', 'font':
 dict(size=16)}}, image='png')
Out[90]: 'file:///home/nbuser/library/temp-plot.html'


# In[50]:


from plotly import __version__
from plotly.offline import download_plotlyjs,init_notebook_mode, plot
#, iplot init_notebook_mode(connected=True)
print (__version__)


# In[51]:


import plotly.graph_objs as go
plot([go.Scatter(x=[95, 77, 84], y=[75, 67, 56])])


# In[54]:


df = pd.DataFrame(np.random.randn(200,6),index= pd.date_range('1/9/2009', periods=200), columns= list('ABCDEF'))


# In[55]:


df.plot(figsize=(20, 10)).legend(bbox_to_anchor=(1, 1))


# In[56]:


df.head()


# In[57]:


df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb',
'March','April', 'May'])


# In[58]:


df.plot.bar(figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[60]:


df.plot.bar(stacked=True,
figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[61]:


df.plot.barh(stacked=True,
figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[65]:


df.plot.hist(bins= 20, figsize=(10,8)).legend
bbox_to_anchor=(1.2, 1)


# ## Multiple Histograms per Column

# In[66]:


df=pd.DataFrame({'April':np.random.randn(1000)+1,'May':np.random.
randn(1000),'June': np.random.randn(1000) - 1}, columns=['April',
'May', 'June'])
df.hist(bins=20)


# In[67]:


df.head()


# ## Creating a Box Plot

# In[69]:


df = pd.DataFrame(np.random.rand(20,5),
columns=['Jan','Feb','March','April', 'May'])
df.plot.box()


# ## Creating an Area Plot

# In[72]:


df.plot.area(figsize=(6, 4)).legend
(bbox_to_anchor=(1.3, 1))


# In[75]:


df = pd.DataFrame(np.random.rand(20,5),
columns= ['Jan','Feb','March','April', 'May'])
df.plot.area(figsize=(6, 4)).legend
bbox_to_anchor=(1.3, 1)


# ## Creating a Scatter Plot

# In[79]:


df.plot.scatter(x='Feb', y='Jan', title='Temperature over two months')


# In[ ]:




