#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import warnings


# In[15]:


warnings.filterwarnings("ignore")


# In[16]:


df = pd.read_csv('company descriptions.csv', encoding="latin-1")


# In[17]:


df = df.drop(['company_description'], axis=1)
original_df = pd.DataFrame(df)


# In[18]:




# In[19]:


final_data = []
for i, row in df.iterrows():
    company_vectorized = []
    company = row['company_short_description']
    company_all = company.split(sep=" ")
    for company_w in  company_all:
        try:
            company_vectorized.append(list(model[company_w]))
        except Exception as e:
            pass
    try:
        company_vectorized = np.asarray(company_vectorized)
        company_vectorized_mean = list(np.mean(company_vectorized, axis=0))
    except Exception as e:
        company_vectorized_mean = list(np.zeros(100))
        pass
    try:
        len(company_vectorized_mean)
    except:
        company_vectorized_mean = list(np.zeros(100))
    temp_row = np.asarray(company_vectorized_mean)
    final_data.append(temp_row)
X = np.asarray(final_data) 


# In[20]:


clf = KMeans(n_clusters=10, n_jobs=-1, max_iter=50000, random_state=1)
clf.fit(X)
print('complete')


# In[23]:


company_name = clf.labels_
company_cluster_df = pd.DataFrame(original_df)
company_cluster_df['company_name'] = np.nan
company_cluster_df['company_name'] = company_name


# In[25]:


company_cluster_df.to_csv('./company_cluster.csv', index=False)


# In[ ]:




