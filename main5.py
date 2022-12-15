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

