#!/usr/bin/env python
# coding: utf-8

# # SEABORN

# ## UNIVERSE PLOTS

# ### 1. Histogram

# In[1]:


import seaborn as sns


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np


# #### Generate Random Data

# In[6]:


data=np.random.randn(100)


# #### Create a Histogram

# In[10]:


sns.histplot(data,bins=30,color="blue")


# In[8]:


plt.title("UNIVARIATE PLOT-HISTOGRAM")


# In[11]:


plt.xlabel("VALUE")


# In[12]:


plt.ylabel("FREQUENCY")


# In[13]:


plt.show()


# In[15]:


sns.histplot(data,bins=30,color="blue")
plt.title("UNIVARIATE PLOT-HISTOGRAM")
plt.xlabel("VALUE")
plt.ylabel("FREQUENCY")


# ## 2. KDE Plot(Kernel Density Estimate)

# In[16]:


import seaborn as sns


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


import numpy as np


# ### Generate Random Data

# In[19]:


data=np.random.randn(50)


# ### Create a Histogram

# In[21]:


sns.kdeplot(data,shade=True,color="red")


# In[22]:


plt.title("UNIVARIENTE PLOT_KDE")


# In[24]:


plt.xlabel("Value")


# In[25]:


plt.ylabel("Density")


# In[26]:


sns.kdeplot(data,shade=True,color="red")
plt.title("UNIVARIENTE PLOT_KDE")
plt.xlabel("Value")
plt.ylabel("Density")


# ## 3. BOX PLOT

# In[27]:


import seaborn as sns


# In[28]:


import matplotlib.pyplot as plt


# In[29]:


import numpy as np


# ### Generate Random Data

# In[ ]:


data=np.random.randn(30)


# ### Create a Box Plot

# In[30]:


sns.boxplot(x=data, color="cyan")


# In[31]:


plt.title("Univariate Plot - Box Plot")


# In[32]:


plt.xlabel("Value")


# In[33]:


sns.boxplot(x=data, color="cyan")
plt.title("Univariate Plot - Box Plot")
plt.xlabel("Value")
plt.show()


# ## 4. VIOLIN PLOT

# In[34]:


import seaborn as sns


# In[35]:


import matplotlib.pyplot as plt


# In[36]:


import numpy as np


# ### Generate Random Data

# In[41]:


data=np.random.randn(500)


# ### Create a Violin Plot

# In[42]:


sns.violinplot(x=data, color="purple")


# In[43]:


plt.title("Univariate Plot - Violin Plot")


# In[44]:


plt.xlabel("Value")


# In[45]:


sns.violinplot(x=data, color="purple")
plt.title("Univariate Plot - Violin Plot")
plt.xlabel("Value")
plt.show()


# # BIVARIATE PLOTS

# ## 1. Scatter Plot

# In[46]:


import seaborn as sns


# In[47]:


import matplotlib.pyplot as plt


# In[48]:


import numpy as np


# #### Generate Random Data

# In[49]:


x = np.random.rand(100)


# In[50]:


y = np.random.rand(100)


# In[51]:


sns.scatterplot(x=x, y=y, color="green")


# In[53]:


plt.title("Bivariate Plot - Scatter Plot")


# In[54]:


plt.xlabel("X-axis")


# In[55]:


plt.ylabel("Y-axis")


# In[56]:


sns.scatterplot(x=x, y=y, color="green")
plt.title("Bivariate Plot - Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ## 2.Line Plot

# In[57]:


import seaborn as sns


# In[58]:


import matplotlib.pyplot as plt


# In[59]:


import numpy as np


# #### Generate Random Data

# In[60]:


x = np.linspace(0, 10, 100)


# In[61]:


y = np.sin(x)


# In[62]:


sns.lineplot(x=x, y=y, color="blue")


# In[63]:


plt.title("Bivariate Plot - Line Plot")


# In[64]:


plt.xlabel("X-axis")


# In[65]:


plt.xlabel("Y-axis")


# In[66]:


sns.lineplot(x=x, y=y, color="blue")
plt.title("Bivariate Plot - Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ## 2. HEATMAP

# In[67]:


import seaborn as sns


# In[68]:


import matplotlib.pyplot as plt


# In[69]:


import numpy as np


# ### Generate Random Data

# In[70]:


data = np.random.rand(10, 10)


# In[71]:


sns.heatmap(data, annot=True, cmap="coolwarm")


# In[72]:


plt.title("Bivariate Plot - Heatmap")


# In[73]:


sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Bivariate Plot - Heatmap")
plt.show()


# ## 3. Bar Plot

# In[74]:


import seaborn as sns


# In[75]:


import matplotlib.pyplot as plt


# In[76]:


import numpy as np


# ### Generate Random Data

# In[77]:


categories = ["A", "B", "C"]


# In[78]:


values = [10, 20, 15]


# In[79]:


sns.barplot(x=categories, y=values, palette="muted")


# In[80]:


plt.title("Bivariate Plot - Bar Plot")


# In[81]:


plt.xlabel("Categories")


# In[82]:


plt.ylabel("Values")


# In[83]:


sns.barplot(x=categories, y=values, palette="muted")
plt.title("Bivariate Plot - Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


# ## 4.Pair Plot : (Special Bivariate Plot)

# In[91]:


import pandas as pd


# ### Generate Random Data

# In[92]:


data = pd.DataFrame({"X": np.random.rand(50),
"Y": np.random.rand(50),
"Z": np.random.rand(50)
})


# In[93]:


sns.pairplot(data)


# In[94]:


plt.suptitle("Bivariate Plot - Pair Plot", y=1.02)


# In[95]:


sns.pairplot(data)
plt.suptitle("Bivariate Plot - Pair Plot", y=1.02)
plt.show()


# In[ ]:




