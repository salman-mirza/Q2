#!/usr/bin/env python
# coding: utf-8

# # Using 50 members of NumPy

# In[46]:


import numpy as np
data = np.random.randn(3,3)
data


# In[47]:


data.shape


# In[48]:


data.dtype


# In[49]:


array1 = np.array(data)
array1


# In[50]:


array2 = np.array([1,2,3,4,5,6])
array2


# In[51]:


array3 = np.array([[1,2,3], [4,5,6,7]])
array3


# In[52]:


data.ndim


# In[53]:


np.zeros(20)


# In[54]:


np.zeros((3,3))


# In[55]:


np.empty((2,3,2))


# In[56]:


np.arange(15)


# In[57]:


np.ones(25)


# In[58]:


np.ones((1,2,3))


# In[59]:


np.asarray(array1)


# In[60]:


np.ones_like((1,2,3))


# In[61]:


np.zeros_like(np.zeros(2))


# In[62]:


np.eye(10)


# In[63]:


np.identity(11)


# In[ ]:




