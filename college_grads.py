import pandas
import numpy
import operator
all_ages = pandas.read_csv('/Users/shreyasramani/Desktop/Data_sets/all-ages.csv')
recent_grads = pandas.read_csv('/Users/shreyasramani/Desktop/Data_sets/recent-grads.csv')
majors = all_ages['Major'].value_counts().index
recent_grads_better = []
all_ages_better = []
for major in majors:
    recent_grads_row = recent_grads[recent_grads['Major']==major]
    all_ages_row = all_ages[all_ages['Major']==major]
    
    recent_grads_unemp_rate = recent_grads_row['Unemployment_rate'].values[0]
    all_ages_unemp_rate = all_ages_row['Unemployment_rate'].values[0]
    
    if all_ages_unemp_rate > recent_grads_unemp_rate:
        all_ages_better.append(major)
    elif all_ages_unemp_rate < recent_grads_unemp_rate:
        recent_grads_better.append(major)
all_ages_dict = {}
recent_grads_dict = {}

for major in all_ages_better:
    major_category = all_ages[all_ages['Major']==major]['Major_category'].values[0]
    all_ages_dict[major_category] = all_ages_dict.get(major_category,0) + 1

for major in recent_grads_better:
    major_category = recent_grads[recent_grads['Major']==major]['Major_category'].values[0]
    recent_grads_dict[major_category] = recent_grads_dict.get(major_category,0) + 1

for w in sorted(all_ages_dict, key=all_ages_dict.get, reverse=True):
  print (w, all_ages_dict[w])

for w in sorted(recent_grads_dict, key=recent_grads_dict.get, reverse=True):
  print (w, recent_grads_dict[w])