# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear 
# (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

cost = 3
days_rented = 9
price_per_movie = days_rented * cost
print(price_per_movie)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they 
# pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_rate = 400
amazon_rate = 380
facebook_rate = 350
payment = (facebook_rate * 10) + (google_rate * 6) + (amazon_rate * 4)
print(payment)

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

is_class_full = False
class_conflict = False
can_enroll = not is_class_full and not class_conflict 
print(can_enroll)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

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


