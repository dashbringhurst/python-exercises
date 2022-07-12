# Identify the data type of the following values:

# 99.9
type(99.9)

# "False"
type("False")

# False
type(False)

# '0'
type('0')

# 0
type(0)

# True
type(True)

# 'True'
type('True')

# [{}]
type[{}]

# {'a': []}
type{'a': []}

# For each of the following code blocks, read the expression and predict what the result of evaluating 
# it would be, then execute the expression in your Python REPL.

'1' + 2
# returns error

6 % 4
# 2

type(6 % 4)
# int

type(type(6 % 4))
# type

'3 + 4 is ' + 3 + 4
# returns error; possible fix: f'3 + 4 is {3 + 4}'

0 < 0
# False

'False' == False
# False

True == 'True'
# False 

5 >= -5
# True

True or "42"
# True

6 % 5
# 1

5 < 4 and 1 == 1
# False

'codeup' == 'codeup' and 'codeup' == 'Codeup'
# False

4 >= 0 and 1 !== '1'
# invalid syntax

6 % 3 == 0
# True

5 % 2 != 0
# True

[1] + 2
# returns error

[1] + [2]
# [1, 2]

[1] * 2
# [1, 1]

[1] * [2]
# returns error

[] + [] == []
# True

{} + {}
# returns error

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear 
# (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

cost_per_day = 3
mermaid_days = 3
bear_days = 5
herc_days = 1
days_rented = mermaid_days + bear_days + herc_days
price = days_rented * cost_per_day
print(price)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they 
# pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_rate = 400
amazon_rate = 380
facebook_rate = 350
fb_hours = 10
goog_hours = 6
amaz_hours = 4
payment = (facebook_rate * fb_hours) + (google_rate * goog_hours) + (amazon_rate * amaz_hours)
print(payment)

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

is_class_full = False
class_conflict = False
can_enroll = not is_class_full and not class_conflict 
print(can_enroll)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 

offer_expired = False
enough_items = True
product_offer = enough_items and not offer_expired
print(product_offer)

# Premium members do not need to buy a specific amount of products.

offer_expired = False
enough_items = False
premium_member = True
product_offer = (enough_items or premium_member) and not offer_expired
print(product_offer)

# Continue working in your data_types_and_variables.py file. 
# Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters

(len)username >= 5

# the username must be no more than 20 characters

(len)username <= 20

# the password must not be the same as the username

username != password

# bonus neither the username or password can start or end with whitespace

username[0] != ' ' and username[-1] != ' '

