lst1=[]

lst2=[20,20.6,"shivam",'shARma',2419]

len_lst2=len(lst2)
print(len_lst2)

print("first item ",lst2[0])

print("middle item ",lst2[len_lst2//2])

print("first item ",lst2[-1])

mixed_data=['Shivam',18,5.6,'married','kyu batau?']

it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle',"Amazon"]

print(it_companies)

len_companies=len(it_companies)

print(len_companies)

print("first item ",it_companies[0])

print("middle item ",it_companies[(len_companies//2)])

print("first item ",it_companies[-1])

it_companies[2]='Tata elxsi'

print(it_companies)

it_companies.append("Adani port")

#middle adding program
#will do it later


it_companies[1]=it_companies[1].upper()

#it_companies.join("#")

if "IBM" in it_companies:
    print("Yes !! IBM is in the list")

it_companies.sort()
print("sorted list ",it_companies)

print(it_companies.reverse())

# print(it_companies.slice[0:3])

