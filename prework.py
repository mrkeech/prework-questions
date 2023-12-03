# Question 1 "Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
#  The first line of the code has been defined as below."

def hello_name(user_name):
    """"Display Greeting"""
    print('"hello_' + user_name + '!"')

hello_name('mrkeech')

# Question 2

def first_odds():
    """Prints odd numbers to 100"""
    x = 0
    while x < 100:
        x +=1 
        if x % 2 == 0:
            continue
        print(x)

first_odds()

# Question 3 "Please write a Python function, 
# max_num_in_list to return the max number of a given list. The first line of the code has been defined as below."

def max_num_in_list(a_list):
    """Shows max number in a list"""
    return max(a_list)

numbers = [1,2,3,4,5,6]
print(max_num_in_list(numbers))

# Question 4 "Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100,
#  unless it is also divisible by 400. The return should be boolean Type (true/false)."

def is_leap_year(a_year):
    """Returns if a given year is a leap year"""
    if a_year % 4 == 0 and a_year % 100 != 0:
         return True
    elif a_year % 100 == 0:
         return False
    elif a_year % 400 == 0:
         return True
    else:
         return False
         
    
print(is_leap_year(2004))

# Question 5 "Write a function to check to see if all numbers in list are consecutive numbers. For example,
#  [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type."

def is_consecutive(a_list):
    """Determines if a given list has consecutive integers"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
    

a_list = [1,2,3,4]
print(is_consecutive(a_list))