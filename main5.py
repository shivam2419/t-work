# first question
def add(a,b):
    return a+b

add(10,20)

#second question
def aoc(r):
    print("Area of circle :- ",3.14*r*r)

r=int(input("Enter radius of circle :- "))
aoc(r)

# third question



#fourth question
def temp(c):
    f=(c*9/5)+32
    print("Temprature in ferhanite = ",f)

c=float(input("Enter temprature in celcius :- "))
temp(c)

#fifth question
def check_season(val):
    season1=['september',"october","november"]
    season2=['december',"january","february"]
    season3=['march',"april","may"]
    season4=['june',"july","august"]

    
    if val in season1:
        print("Season is Autumn")
    if val in season2:
        print("Season is winter")
    if val in season3:
        print("Season is spring")
    if val in season4:
        print("Season is zummer")

val=input("Enter month :- ")
check_season(val)

#sixth question

#seventh question
import math
def solve_quadratic_eqn():
    a=int(input("Enter value of A :- "))
    b=int(input("Enter value of B :- "))
    c=int(input("Enter value of C :- "))
    
    d=(b*b)-(4*a*c)
    d=d*d
    print(f"Your quadratic equation is :- {a}x^2 + {b}x + {c}")
    x1=((-b+math.sqrt(d))/2*a)
    x2=(-b-math.sqrt(d))/2*a
    print()
    return f"x={x1} , x={x2}"
v=solve_quadratic_eqn()
print(v)
 
#eight question 

def print_list(a):
    for i in a:
        print(i)
a=[2,4,3,57,3]
print_list(a)

#ninth question

lst=[1,2,3,4]
lst.reverse()
print(lst)

#tenth question
def capitalize_list_items(a):
    new=[]
    for i in a:
        i=str(i)
        item=i.upper()
        new.append(item)
    print(new)

a=["shivam","shyam","ram","mohan"]
capitalize_list_items(a)

#eleventh question

def add_item(item,item2):
    lst=["item1","item2"]
    lst.append(item)
    lst.append(item2)
    print(lst)
val="item3"
val2="item4"
add_item(val,val2)


#twelfth question
def add_item(food_staff,val):
    food_staff.append(val)
    print(food_staff)

food_staff=['Potato','Tomato','Mango']
val=input("What you wann add ? ")
add_item(food_staff,val)

#thirteen question
def remove_item(lst,item):
    lst.remove(item)
    print(lst)

lst=[1,2,3,4,5,6]
val=5
remove_item(lst,val)

#fourteen question

def remove_item2(food_staff,val):
    
    food_staff.remove(val)
    print(food_staff)

food_staff=['Potato','Tomato','Mango']
print("Your list :- ",food_staff)
val=input("What you wann remove ? ")
remove_item2(food_staff,val)

#fifteen question
def sum_of_numbers(a):
    val=0
    for i in range(a+1):
        val+=i
    print("Sum till number",a,":- ",val)

a=int(input("Enter number :- "))
sum_of_numbers(a)

#sixteen question
def sum_of_odds(a):
    val=0
    
    for i in range(a+1):
        if i%2!=0:
            val+=i
    print("Sum till number",a,":- ",val)

a=int(input("Enter number :- "))
sum_of_odds(a)

#seventeen question
def sum_of_even(a):
    val=0
    
    for i in range(a+1):
        if i%2==0:
            val+=i
    print("Sum till number",a,":- ",val)

a=int(input("Enter number :- "))
sum_of_even(a)

#EXERCISE LEVEL :- 2

#Eighteen question
def even_and_odds(num):
    pos=0
    neg=0
    for i in range(0,num+1):
        if i%2==0:
            pos+=1
        else:
            neg+=1
    print("Total EVEN number :- ",pos)
    print("Total ODD number :- ",neg)

num=int(input("Enter number :- "))
even_and_odds(num)

#Ninteen question
def factorial (num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("Factorial of ",num,"is",fact)

num=int(input("Enter number :- "))
factorial(num)

#Twenty question


#Twenty one question

def calculate(lst):
    # solving mean
    sum=0
    length=len(lst)
    for i in (lst):
        sum+=i
    
    mean=sum/length

    #solving median
    if length%2==0:
        median=(length)//2
        median=lst[median-1]
    else:
        median=(length+1)//2
        median=lst[median-1]

    #solving mode
    mode=None
    #solving range
    rangee=None
    #solving range
    variance=None
    #solving range
    std=None
    print("MEAN :- ",mean)
    print("MEDIAN :- ",median)
    print("MODE :- ",mode)
    print("RANGE :- ",rangee)
    print("VARIANCE :- ",variance)
    print("STABDARD DEVIATIOn :- ",std)
    


lst=[2,4,3,5,7,9,1]
print("ELEMNETS = ",lst)
calculate(lst)

#EXERCISE LEVEL :-  3

#first question
def is_prime(num):
    for i in range(2,num):
        if num%i!=0:
            ans="Yes,it is a prime number..."
        else:
            ans="No,it is not a prime number..."
            break
    print(ans)

num=int(input("Enter number :- "))
is_prime(num)

#second question

def unique():
    lst=[1,3,2,4]
    new_lst=[]

    for i in lst:
        if i in new_lst:
            print("Items are not unique")
            val=0
            break
        else:
            new_lst.append(i)
            val=1
    
    if val==1:
        print("Items are unique")
        

unique()


#Third question

def same_data_type():
    lst=[1,2.2,"Hello"]
    new_lst=[]

    for i in lst:
        dtype=type(i)
        new_lst.append(dtype)

    for j in new_lst:
        if new_lst.count(j)>1:  
            ans="Some values are of same data type"
        else:
            ans="Values are of different data types "
    print(ans)

same_data_type()

#Fourth question

def var(var):
    ans=var.isidentifier()
    if ans:
        print("Yes,It is a valid variable")
    else:
        print("No,It is not a valid variable ")

var1=input("Enter variable :- ")
var(var1)

#Fifth question
from data import countries_data

countries_data.fun() #<-- fun() is a function in countries data file


#sixth question

def most_spoken_languages():   
    ans=['English','Mandarin Chinese','Hindi','Spanish','French','Bengali','Modern Arabic','Portuguese']
    print("Your list :- ",ans)
    ans.sort()
    ans.reverse()
    print("Answer in descending order :- ",ans)

most_spoken_languages()

#seventh question

def most_populated_countries():   
    ans=['China','India','USA','Indonesia','Pakistan','Brazil','Nigeria','Bangladesh','Russia','Mexico']
    print("Your list :- ",ans)
    ans.sort()
    ans.reverse()
    print("Answer in descending order :- ",ans)

most_populated_countries()
