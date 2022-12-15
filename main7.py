#returns perfect square till n number 
def perfect_square(n):
    lst=[]
    for i in range(0,n+1):
        val=i*i
        lst.append(val)

    print("List :- ",lst)

n=int(input("Enter number :- "))
perfect_square(n)