#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Define a function named is_two. It should accept one input and return True if the passed 
# input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False


# In[4]:


is_two('e')


# In[5]:


is_two('2')


# In[6]:


# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.
vowels = list('aeiouAEIOU')
def is_vowel(x):
    if x in vowels:
        return True
    else:
        return False
    


# In[7]:


is_vowel('ef')


# In[8]:


is_vowel('ae')


# In[9]:


is_vowel('I')


# In[10]:


# Define a function named is_consonant. It should return True if the passed string is 
# a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    if is_vowel(x) == False: 
        return True
    else:
        return False


# In[11]:


is_consonant('i')


# In[52]:


is_consonant('q')


# In[74]:


# Define a function that accepts a string that is a word. The function should capitalize 
# the first letter of the word if the word starts with a consonant.

def capitalize_word(x):
    for letter in x:
        if is_consonant(letter) == True:
            return x.capitalize()
        else:
            return x


# In[78]:


capitalize_word('hurrah')


# In[79]:


# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(p, b):
    tip = p * b
    return round(tip, 2)


# In[80]:


calculate_tip(.12, 26.76)


# In[81]:


# Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(x, y):
    discount_price = x - (x * (y / 100))
    return round(discount_price, 2)


# In[82]:


apply_discount(178.50, 10)


# In[83]:


# Define a function named handle_commas. It should accept a string that is a number 
# that contains commas in it as input, and return a number as output.

def handle_commas(string):
    for character in ',':
        string = string.replace(character, '')
    return int(string)
   


# In[84]:


handle_commas('4,0,0,0')


# In[85]:


# Define a function named get_letter_grade. It should accept a number and return the 
# letter grade associated with that number (A-F).

def get_letter_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    return 'F'


# In[86]:


get_letter_grade(65)


# In[87]:


# Define a function named remove_vowels that accepts a string and returns a string 
# with all the vowels removed.

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    for item in string:
        if item == item in vowels:
            string = string.replace(item, '')
    return string


# In[88]:


remove_vowels('gunrunner')


# In[89]:


# Define a function named normalize_name. It should accept a string and return a valid 
# python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(string):
    forbidden_chars = '!@#$%^&*()-+{}[]\|;:\'\"/?.><,`~\\'
    for item in string:
        if item in forbidden_chars:
            string = string.replace(item, '')
    string = string.strip()
    string = string.lower()
    string = string.replace(' ', '_')
    return string
    


# In[90]:


normalize_name(' How%dy Ho ! ')


# In[91]:


# Write a function named cumulative_sum that accepts a list of numbers and returns 
# a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(x):
    cumulative_list = []
    csum = 0
    for number in x:
        csum += number
        cumulative_list.append(csum)
    return cumulative_list
        


# In[92]:


cumulative_sum([1, 2, 3, 4])


# In[93]:


# Once you've completed the above exercises, follow the directions from 
# https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.


# In[348]:


# Create a function named twelveto24. It should accept a string in the format 
# 10:45am or 4:30pm and return a string that is the representation of the time 
# in a 24-hour format. Bonus write a function that does the opposite.

def twelveto24(string):
    if string[0:2].isdigit() and 'pm' in string:
        string = string.replace(':', '')
        hour = (int(string[0:2]) + 12)
        if hour == 24:
            hour = '00'
        string = string.replace(string[0:2],str(hour))
        string = string.replace('pm', '')
    elif string[0:1].isdigit() and 'pm' in string:
        hour = (int(string[0:1]) + 12)
        string = string.replace(string[0:1],str(hour))
        string = string.replace('pm', '')
        string = string.replace(':', '')
    else:
        hour = int(string[0:1])
        if hour < 10:
            hour = '0' + (str(hour))
        string = string.replace(string[0:1],str(hour))
        string = string.replace('pm', '')
        string = string.replace(':', '')
        string = string.replace('am', '')
    return string
       


# In[349]:


twelveto24('1:34am')


# In[350]:


twelveto24('11:34pm')


# In[385]:


# Create a function named col_index. It should accept a spreadsheet column name, 
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

def col_index(x):
    for item in x:
        if len(x) == 1:
            item = ord(x) - 64
        if len(x) != 1:
            i = x[0]
            j = x[1]
            item = ord(j) - 38
        return item


# In[386]:


col_index('A')


# In[389]:


col_index('AZ')


# In[ ]:





# In[ ]:




