#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Read the files
df_ny = pd.read_csv('new_york_city.csv')
df_chicago = pd.read_csv('chicago.csv')
df_washington = pd.read_csv('washington.csv')

# Diaplay the first 5 rows of each dataframe
print(df_ny.head())
print(df_chicago.head())
print(df_washington.head())


# In[4]:


# convert Start Time and End Time to datetime
df_ny['Start Time'] = pd.to_datetime(df_ny['Start Time'])
df_ny['End Time'] = pd.to_datetime(df_ny['End Time'])

df_chicago['Start Time'] = pd.to_datetime(df_chicago['Start Time'])
df_chicago['End Time'] = pd.to_datetime(df_chicago['End Time'])

df_washington['Start Time'] = pd.to_datetime(df_washington['Start Time'])
df_washington['End Time'] = pd.to_datetime(df_washington['End Time'])


# In[60]:


def popular_times_of_travel(df):
    most_common_month = df['Start Time'].dt.month.value_counts().index[0]
    most_common_dayofweek_nr = df['Start Time'].dt.dayofweek.value_counts().index[0]
    most_common_hour = df['Start Time'].dt.hour.value_counts().index[0]

    weekday_dict = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    months = ["NA",
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

    print('most common month = ',months[most_common_month])
    print('most common day of week = ',weekday_dict[most_common_dayofweek_nr])
    print('most common hour = ',most_common_hour)


# In[61]:


print('Popular times of travel - New York')
popular_times_of_travel(df_ny)


# In[62]:


print('Popular times of travel - Chicago')
popular_times_of_travel(df_chicago)


# In[63]:


print('Popular times of travel - Washington')
popular_times_of_travel(df_washington)


# In[54]:


def popular_stations_trips(df):
    MostCommonStartStation = df['Start Station'].value_counts().index[0]
    MostCommonEndStation = df['End Station'].value_counts().index[0]
    mostCommonCombination = df.groupby(['Start Station','End Station']).size().idxmax()
    
    print('Most common start station: ',MostCommonStartStation)
    print('Most common end station: ',MostCommonEndStation)
    print('Most Common Combination of Start and End Station: ',mostCommonCombination)


# In[55]:


print('Popular stations and trips - New York')
popular_stations_trips(df_ny)


# In[56]:


print('Popular stations and trips - Chicago')
popular_stations_trips(df_chicago)


# In[57]:


print('Popular stations and trips - Washington')
popular_stations_trips(df_washington)


# In[47]:


df = pd.read_csv('test.csv')


# In[50]:


def trip_duration(df):
    totalTravelTime = df['Trip Duration'].sum()
    avgTravelTime = df['Trip Duration'].mean()
    

    print('Total travel time = {} mins'.format(totalTravelTime))
    print('Average travel time = {} mins'.format(avgTravelTime))
    


# In[51]:


print('Trip duration - New York')
trip_duration(df_ny)


# In[52]:


print('Trip duration - Chicago')
trip_duration(df_chicago)


# In[53]:


print('Trip duration - Washington')
trip_duration(df_washington)


# In[35]:


def user_info(df):
    countUserType = df['User Type'].value_counts()

    print('count User Type = ')
    print(countUserType)
    print('')

    if 'Gender' in df.columns:
        countGender = df['Gender'].value_counts()
        print(countGender)
    
    print('')
    if 'Birth Year' in df.columns:

        birthYear = df['Birth Year'].dropna()
        earliestYearOfBirth = birthYear.sort_values().values[0]
        mostRecentYearOfBirth = birthYear.sort_values().values[-1]
        mostCommonYearOfBirth = birthYear.value_counts().index.values[0]

        print('earliest year of birth =' , int(earliestYearOfBirth))
        print('most recent year of birth =' , int(mostRecentYearOfBirth))
        print('most common year of birth',int(mostCommonYearOfBirth))


# In[36]:


print('User info - New York')
user_info(df_ny)


# In[37]:


print('User info - Chicago')
user_info(df_chicago)


# In[38]:


print('User info - Washington')
user_info(df_washington)


# In[ ]:




