
# coding: utf-8

# In[7]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().magic('matplotlib inline')
pixar_movies = pd.read_csv('PixarMovies.csv')
dims = pixar_movies.shape
print (dims)
print(pixar_movies.head(dims[0]))
print(pixar_movies.dtypes)
print(pixar_movies.describe())


# In[8]:

pixar_movies['Domestic %'] = pixar_movies['Domestic %'].str.rstrip('%').astype(float)
pixar_movies['International %'] = pixar_movies['International %'].str.rstrip('%').astype(float)
pixar_movies['IMDB Score'] = pixar_movies['IMDB Score'] * 10
filtered_pixar = pixar_movies.loc[0:13]
pixar_movies.set_index('Movie', inplace=True)
filtered_pixar.set_index('Movie',inplace=True)


# In[9]:

critics_reviews = pixar_movies[['RT Score','IMDB Score','Metacritic Score']]
critics_reviews.plot(figsize=(10,6))
plt.show()
critics_reviews.plot(kind='box',figsize=(9,5))
plt.show()


# In[10]:

revenue_proportions = filtered_pixar[['Domestic %','International %']]
revenue_proportions.plot(kind='bar',stacked=True)


# In[11]:

oscars = filtered_pixar[['Oscars Nominated','Oscars Won']]
oscars.plot(kind='bar')


# In[12]:

pixar_movies['Mean Score'] = critics_reviews.apply(lambda x: np.mean(x),axis=1)
dom_gross = pixar_movies[['Adjusted Domestic Gross','Production Budget','Mean Score']]
sns.pairplot(dom_gross)


# In[ ]:



