#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium 
import pandas as pd


# In[19]:


geodata = pd.read_csv("/Users/yliu/Desktop/thesis/code/data/tests/geodata.csv")
# geodata['city_states'].dtype


# In[52]:


geodata = geodata[geodata['lon'].notnull()]
geodata


# In[57]:


m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)


# In[58]:


for i in range(0,len(geodata)):
   folium.Circle(
      location=[geodata.iloc[i]['lat'], geodata.iloc[i]['lon']],
      popup=[geodata.iloc[i]['city_states'], geodata.iloc[i]['tribute_val']],
      radius=float(geodata.iloc[i]['tribute_val'])*2000,
      color='crimson',
      fill=True,
      fill_color='crimson'
   ).add_to(m)


# In[59]:


m


# In[ ]:




