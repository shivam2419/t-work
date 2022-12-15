fruits=['banana','orange','mango','lemon']

check=input("Enter new fruit or check :- ")

if check in fruits:
    print(check,"in list")
    print(fruits)
else:
    fruits.append(check)
    print("item added !!")
    print(fruits)