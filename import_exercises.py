#!/usr/bin/env python
# coding: utf-8

# In[992]:


import math


# In[993]:


# When calling a function from an imported module, use module_name.function_name
math.pi


# In[994]:


math.sqrt(64)


# In[995]:


from math import sqrt
sqrt(100)


# In[996]:


import numpy as np


# In[997]:


np.arange(10)


# In[998]:


import pandas as pd


# In[999]:


pd.Series((np.arange(5)))


# In[1000]:


# Import and test 3 of the functions from your functions exercise file. 
# Import each function in a different way:

# Run an interactive python session and import the module. 
# Call the is_vowel function using the . syntax.

import functions_exercises


# In[1001]:


functions_exercises.is_vowel('O')


# In[1002]:


# Create a file named import_exericses.py. 
# Within this file, use from to import the calculate_tip function directly. 
# Call this function with values you choose and print the result.


# In[1003]:


# Create a jupyter notebook named import_exercises.ipynb. 
# Use from to import the get_letter_grade function and give it an alias. 
# Test this function in your notebook.
# Make sure your code that tests the function imports is run from the same directory 
# that your functions exercise file is in.

from functions_exercises import get_letter_grade as lg

lg(76)


# In[1004]:


# Read about and use the itertools module from the python standard library to help you 
# solve the following problems:

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different combinations are there of 2 letters from "abcd"?
# How many different permutations are there of 2 letters from "abcd"?

import itertools


# In[1005]:


list(itertools.permutations('abcd', 2))


# In[ ]:





# In[1006]:


import json


# In[1007]:


profiles = json.load(open('profiles.json'))


# In[1008]:


# Using this data, write some code that calculates and outputs the following information:


# In[1009]:


# Total number of users

len(profiles)


# In[1010]:


# Number of active users

def active_users(x):
    total = 0
    for i in x:
        if (i['isActive']) == True:
            total += 1
    return total


# In[1011]:


active_users(profiles)


# In[1012]:


# Number of inactive users

def inactive_users(x):
    total = 0
    for i in x:
        if (i['isActive']) == False:
            total += 1
    return total


# In[1013]:


inactive_users(profiles)


# In[1014]:


# Grand total of balances for all users

def balances(x):
    sum_amt = 0
    for i in x:
        list_of_balances = []
        balance = i['balance']
        balance = balance.replace('$', '')
        balance = balance.replace(',', '')
        list_of_balances.append(float(balance))
        for amt in list_of_balances:
            sum_amt += amt
    return sum_amt


# In[1015]:


balances(profiles)


# In[1016]:


# Average balance per user

round(total_balances(profiles) / len(profiles), 2)


# In[1017]:


# User with the lowest balance
list_of_balances = []
def lowest_balance(x):
    for i in x:
        balance = i['balance']
        balance = balance.replace('$', '')
        balance = balance.replace(',', '')
        balance = balance.replace('.', '')
        list_of_balances.append(int(balance))
        for i in list_of_balances:
            min_balance = min(list_of_balances)
    return round((min_balance / 100), 2)


# In[1018]:


lowest_balance(profiles)


# In[1019]:


# User with the highest balance

def highest_balance(x):
    max_balance = max(list_of_balances)
    return round((max_balance / 100), 2)


# In[1020]:


highest_balance(profiles)


# In[1021]:


# Most common favorite fruit

from collections import Counter
fruits = []
def most_fav_fruit(x):
    for i in x:
        fruit_type = i['favoriteFruit']
        fruits.append(fruit_type)
    return Counter(fruits).most_common(1)   


# In[1022]:


most_fav_fruit(profiles)


# In[1023]:


# Least common favorite fruit

least_common = []
def least_fav_fruit(x):
    for i in x:
        fruit_type = i['favoriteFruit']
        least_common.append(fruit_type)
    return (Counter(least_common).most_common()[-1])
        
    


# In[1024]:


least_fav_fruit(profiles)


# In[1149]:


# Total number of unread messages for all users

message_count = []
message_total = []
def total_unread_messages(x):
    for i in x:
        messages = i['greeting']
        message_count.append([int(s) for s in messages.split() if s.isdigit()]) 
        
    #print(message_count)
    for item in message_count:    
        for number in item:
            message_total.append(number)
            
    return sum(message_total)


# In[1150]:


total_unread_messages(profiles)


# In[ ]:




