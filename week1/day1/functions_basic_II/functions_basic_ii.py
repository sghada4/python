#Countdown  function
def countdown(x):
    for i in range(x,-1,-1):
        print(i)
countdown(5)
#!output 5 4 3 2 1 0
#Print and Return function
def print_and_return (list):
    print(list[0])
    return list[1]
y=print_and_return([1,2])
print(y) #!if we want to print also the return of the function
print_and_return([1,2])
#First Plus Length
def first_plus_length(list):
    return(list[0]+len(list))
result=first_plus_length([1,2,3,4,5])
print(result)
#Values Greater than Second
def values_greater_than_second(list):
    sum=0
    new_list=[]
    if(len(list)<2):
        return False
    else:
        for i in range(len(list)):
            if(list[i]>list[1]):
                sum+=1
                new_list.append(list[i])
    print(len(new_list))
    return new_list
result1=values_greater_than_second([5,2,3,2,1,4])
print(result1)
result2=values_greater_than_second([5])
print(result2)
#This Length, That Value 
def length_and_value(x,y):
    list=[]
    for i in range(x):
        list.append(y)
    return list
result=length_and_value(6,2)
print(result)