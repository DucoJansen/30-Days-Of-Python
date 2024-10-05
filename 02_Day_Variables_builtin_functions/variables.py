<<<<<<< HEAD
=======

import math
>>>>>>> 2cf695b116db8f657eef828951d538303c7c652e
import numpy as np
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Day 2: 30 Days of python programming
first_name = 'Duco'
last_name = 'Jansen'
full_name = first_name + ' ' + last_name
country = 'Germany'
city = 'Kranenburg'
age = 23
year = 2024
is_married = False
is_true = True
is_light_on = False
multiple, variables, on, one, line = 1,2,3,4,5

print(type(first_name))
print(len(first_name + last_name))

num_one, num_two = 5,4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = np.floor(num_one/num_two)
print(floor_division)
def circleArea(radius):
    return radius**2 * math.pi

def circleCircum(radius):
    return radius*2 * math.pi

print(circleArea(2))

area_of_circle = circleArea(30)
circum_of_circle = circleCircum(30)
radius = input('Enter a circle radius: ')
radius_int = int(radius)
print('Area of circle with radius ',radius,' is: ',circleArea(radius_int))

first_name = input('What is your first name?')
last_name = input('What is your last name?')
country = input('What country are you from')
age = input('How old are you?')
