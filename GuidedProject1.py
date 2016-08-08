
# coding: utf-8

# In[1]:

import pandas as pd
white_house = pd.read_csv("2015_white_house.csv")
print(white_house.shape)


# In[4]:

print(white_house.iloc[white_house.shape[0]-1])


# In[5]:

white_house


# In[5]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
plt.hist(white_house["Salary"])
plt.show()


# So far we have imported the Pandas library, and loaded the data set that was in .csv format into a Pandas dataframe. After this we printed the dimensions of the data frame, printed the last row of the data frame, displayed the full data frame, and plotted a histogram of salaries using matplotlib.

# In[3]:

white_house['Position Length'] = white_house['Position Title'].apply(lambda x: len(x))


# In[6]:

plt.scatter(white_house['Position Length'], white_house['Salary'])


# In[7]:

total_salary = sum(white_house['Salary'])
print(total_salary)


# In[11]:

min_sal = min(white_house['Salary'])
max_sal = max(white_house['Salary'])
lowest_paid = white_house[['Name','Salary']][white_house['Salary']==min_sal]
print(lowest_paid)
highest_paid = white_house[['Name','Salary']][white_house['Salary']==max_sal]
print(highest_paid)


# In[14]:

split_title = white_house['Position Title'].apply(lambda x: x.split())
most_common={}
for title in split_title:
    for word in title:
        most_common[word] = most_common.get(word,0) + 1
for words in sorted(most_common, key=most_common.get, reverse=True):
    print(words, most_common[words])


# In[19]:

first_last = white_house['Name'].apply(lambda x: x.split(' '))
split_name = []
for n in first_last:
    if n[1] == 'Jr.':
        split_first = n[2].split()
    else:
        split_first = n[1].split()
    split_name.append(split_first[0])
most_common_name = {}
for names in split_name:
    most_common_name[names] = most_common_name.get(names,0) + 1
for n in sorted(most_common_name,key=most_common_name.get,reverse=True):
    print(n,most_common_name[n])


# In[ ]:



