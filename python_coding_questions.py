# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
def hello_name(user_name):
    """
    As per instruction, we need to display
    "hello_USERNAME!"
    instead of
    "Hello Username!" or other variations.
    """
    print(f"hello_{user_name.upper()}!")

hello_name('USERNAME')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def first_odds():
    """Display all of the odd numbers from 1 to 100."""
    for odd_number in range(1,100,2):
        print(odd_number)

#I chose to print the function to show that nothing is returned as it says "None" at the end of the odd numbers.
print(first_odds())

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list(a_list):
    """Display the largest number in a list."""
    return max(a_list)

#I printed to verify it works. Feel free to delete the print for the function to simply return.
print(max_num_in_list([2, 4, 6, 0, 1]))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
def is_leap_year(a_year):
    """Return True if the year is a leap year."""
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

#Again, I printed the four different possible outcomes to verify it works.
print(is_leap_year(2))
print(is_leap_year(8))
print(is_leap_year(200))
print(is_leap_year(800))


# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
def is_consecutive(a_list):
    """
    Return True if all numbers in a list are concsecutive,
    but return false if the numbers are not consecutive.
    """
    consecutive = True
    for place_in_list in range(1,len(a_list)):
        """This checks to see if each number in the list is one apart."""
        difference = a_list[place_in_list] - a_list[place_in_list - 1]
        if difference != 1:
            consecutive = False
    return consecutive

# Again, I printed to verify it works.
print(is_consecutive([-2,-1,0,1]))
print(is_consecutive([8,6,7,5,3,0,9]))