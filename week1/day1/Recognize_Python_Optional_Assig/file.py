#single line comment
"""
multiple ligne comment

"""
#Data types
#?primitive type
#* numbers
num1 = 42
num2 = 2.3
#* boolean
boolean = True
#* string
string = 'Hello World'
#?composite type
#*list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#* Dictionaries
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#*tuples
fruit = ('blueberry', 'strawberry', 'banana')
#print type of element
print(type(fruit))
#!tuples
#print the second element in the list
print(pizza_toppings[1])
#!'Sausage'
#add an element to the list at the end
pizza_toppings.append('Mushrooms')
#print the value of the key 'name'from the dict person
print(person['name'])
#!John
#change the value of the key name to George
person['name'] = 'George'
#add a new key to the dict person (eye_color) with the value (blue)
person['eye_color'] = 'blue'
#print the third fruits in the tuples fruit
print(fruit[2])
#!banana
#?conditional
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#!It's lower 
#!Just right!
#?for loop
#print numbers from 0 to 4 incresing by 1 
for x in range(5):
    print(x)
#!0 1 2 3 4
#print numbers from 2 to 4 incresing by 1 
for x in range(2,5):
    print(x)
#!2 3 4
#print numbers from 2 to 9 incresing by 3 
for x in range(2,10,3):
    print(x)
#!2 5 8
#?While loop
#print numbers from 0 to 4 incresing by 1
x = 0
while(x < 5):
    print(x)
    x += 1
#!0 1 2 3 4
#remove from the back (by default)
pizza_toppings.pop()

#delete the second element in the list(pizza_toppings)
pizza_toppings.pop(1)
#print the elements of dict person 
print(person)
#!{'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
#delete the key eye_color from dict person 
person.pop('eye_color')
print(person)
#!{'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# Iterate through a list and print (after first statement) three time untile topping=='olives'
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#!After 1st if statement
#!After 1st if statement
#!After 1st if statement
#?Function
#creat function without parametres to print "hello" 10 times
def print_hello_ten_times():
    for num in range(10):
        print('Hello1')
#call the function print_hello_ten_times
print_hello_ten_times()
#declare a function withe a parametre x
def print_hello_x_times(x):
    for num in range(x):
        print('Hello2')
#call the function print_hello_ten_times with the argument 4 (print hello 4 times)
print_hello_x_times(4)
#function with parametre x = 10 
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello3')
#call the function without argument but withe the parametre x=10 so print hello 10 times
print_hello_x_or_ten_times()
#call the function with the argument 4 so print hello 4 times
print_hello_x_or_ten_times(4)


"""
Bonus section

"""

#print(num3)
#!num3 not defined
num3 = 72
#! define num3 with 72 value
fruit[0] = 'cranberry'
#! fruit is a tuples so it is unchangeble
print(person['favorite_team'])
#!there is no key (favorite_team) in the dict person
print(pizza_toppings[7])
#!the pizza_topping length < 7
#print the default value of type boolean
print(boolean)
#!True
fruit.append('raspberry')
#!fruit is tuples so unchangeble
fruit.pop(1)
#!tuple has no function because it is unchangeble