#!/usr/bin/env python
# coding: utf-8

# In[86]:


import pandas as pd
import numpy as np


# In[87]:


data = pd.read_csv("C:\\Users\\User\\Downloads\\archive\\Netflix Shows.csv")


# In[88]:


data.isnull().sum()


# In[89]:


data.notnull().sum()


# In[20]:


data.head(n=10)


# In[21]:


data.tail(n=10)


# In[22]:


data.shape


# In[23]:


data.columns


# In[24]:


type(data)


# # loc label base selection
# 

# 
# # iloc index label base selection 
# 

# In[25]:


data.loc[data.rating == "PG-13"]


# In[27]:


data.loc[(data.rating == "PG-13" ) & (data['release year'] == 2011)]


# In[30]:


data.loc[ (data['release year'] == 2011)]


# In[44]:


data.loc[(data.rating == "PG-13") & (data['release year'] == (2011 ))]


# In[46]:


data.loc[(data.rating == 'PG') & (data['release year'] == 2011)]


# In[52]:


data.loc[(data.rating == "TV-14") & ((data['user rating score'] >= 95) &( data['user rating score'] <= 100 ))]


# In[55]:


data.loc[(data.rating == "TV-14") , ["title" , "ratingLevel","ratingDescription"]]


# # iloc

# In[58]:


data.iloc[0:4]   # first row than column


# In[68]:


data.iloc[[2,6] , 0:7]


# In[71]:


data.iloc[[2,9] , :-1]


# In[108]:


data.iloc[10:50]


# In[78]:


data.iloc[[3,9] , 2 : 7]


# In[79]:


data.describe()


# In[80]:


data.min()


# In[81]:


data.mean()


# In[82]:


data.count()


# In[85]:


data["user rating score"].mean()


# In[90]:


int(data["user rating score"].mean())


# In[103]:


data.replace(to_replace=np.nan ,value = (int(data["user rating score"].mean())),inplace=True)


# In[93]:


data


# In[94]:


data.head(n=10)


# In[102]:


data.loc[((data["user rating score"] >= 84) & (data["user rating score"] <=90) ) & (data.rating == "TV-14")]


# In[104]:


data.isnull().sum()


# In[107]:


data.notnull().sum()


# In[ ]:




