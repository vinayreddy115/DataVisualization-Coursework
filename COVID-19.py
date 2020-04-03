#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px
import datetime
import os


# In[20]:


os.chdir('D:/USF MS BAIS CourseWork/Sem-2/Data Visualization')


# In[21]:


covid_map = pd.read_csv("time_series_covid19_confirmed_global.csv")


# In[22]:


covid_map.head()


# In[23]:



m = folium.Map(location=[52.667989, -1.464582], zoom_start=1.5 )
for _, row in covid_map.iterrows():
    count_10 = row['Count of Confirmed Cases'] * 4
    country_name = str("country: " + str(row["Country/Region"]))
    confirmed_cases = str("Confirmed: " + str(row["Count of Confirmed Cases"]))
    Death_count = str("Deaths: " + str(row["Overall Death Count"]))
    RecoveredCases_count = str("Recovered: " + str(row["Overall Recovered Cases"]))
    pop_up_data = str(country_name + '\n'+confirmed_cases+'\n'+Death_count+'\n'+RecoveredCases_count)
    folium.Circle([row['Lat'], row['Long']], count_10, fill=False,fill_color='red').add_child(folium.Popup(pop_up_data)).add_to(m)
m

