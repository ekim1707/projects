# 4. Day of the Week
# 
# Given the following code that prompts the user for a day number (the int function converts a numeric string to a number):
# 
# day = int(input('Day (0-6)? '))
# Fill in your code here
# The user will enter a number between 0 to 6 inclusive. Given this number, print a day of the week. 0 for Sunday, 1 for
# Monday, 2 for Tuesday, and so on. Here's an example user session (this assumes you've named the file day_of_week.py):
# 
# $ python day_of_week.py Day (0-6)? 5 Friday $ python day_of_week.py Day (0-6)? 0 Sunday

day = int(input('Day (0-6)? '))
daysofweek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(daysofweek[day])