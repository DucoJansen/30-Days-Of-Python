
import math
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