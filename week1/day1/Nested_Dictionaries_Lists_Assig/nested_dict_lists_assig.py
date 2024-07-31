
#?Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
#!Change the value 10 in x to 15
x[1][0]=15
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#!Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']= "Bryant"
print(students)
#!In the sports_directory, change 'Messi' to 'Mo Salah'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]="Mo Salah"
print(sports_directory)
#!Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)
#?Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(len(students)):
        print(students[i]['first_name'], students[i]['last_name'])
iterateDictionary(students)
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first name - {students[i]['first_name']} last name - {students[i]['last_name']}")
iterateDictionary(students)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

#?Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#?Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key in dojo:
        print(len(dojo[key]), key)
        for i in range(len(dojo[key])):
            print(dojo[key][i])
        print("\n")
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

