#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_excel ('sales dataset.xls')
df.columns = [c.replace(' ', '_') for c in df.columns]


# In[2]:


df.head(10)


# In[2]:


a=df[(df['Sales_Amt']>200)&(df['Pay_Type']=='Credit')].head(5)
dc = pd.DataFrame(a, columns = ['Pay_Type', 'Sales_Qty','Department'])
dc


# In[4]:


df.groupby('Department')[['Sales_Amt']].mean()


# In[4]:


b=df.groupby('Item_Name')[['Sales_Amt','Sales_Qty']].sum()
b


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


plt.plot(df['Sales_Amt'],df['Sales_Qty']);


# In[7]:


plt.hist(df.Sales_Cost,bins=5);


# In[8]:


c=df[df['Item_Name']=='ATT']
d=df[df['Item_Name']=='DVD']


# In[9]:


import numpy as np
plt.hist([c.Sales_Amt,d.Sales_Amt]);
plt.legend(['ATT','DVD']);


# In[10]:


a1=df[(df.Sales_Amt>200)| (df.Sales_Cost<200)]
dc = pd.DataFrame(a1, columns = ['Pay_Type', 'Sales_Qty']).head(5)
dc


# In[11]:


plt.bar(df.Item_Name,df.Sales_Amt,color=['magenta', 'red', 'green', 'blue', 'cyan']);
plt.plot(df.Item_Name,df.Sales_Amt,'o--r');


# In[12]:


sns.barplot(df.Item_Name,df.Sales_Qty,hue=df.Pay_Type);


# In[13]:


fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(24,6))
sns.barplot(df.Item_Name,df.Sales_Qty,ax=axes[1]);
axes[0].plot(df.Department,df.Sales_Cost,'o--r')
sns.barplot(df.Pay_Type,df.Sales_Qty,ax=axes[2])


# In[14]:


d=df[(df['Department']=='Sales')|(df['Sales_Amt']>300)].head(3)
d


# In[15]:


sns.countplot(df['Pay_Type'])


# In[38]:


a2=df['Pay_Type'].value_counts().reset_index()
a2.columns=["Pay_type","Counts"]
sns.barplot(x="Pay_type",y="Counts",data=a2)


# In[35]:





# In[ ]:




