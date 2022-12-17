it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon',}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]
print("IT Companies :- ",it_companies)
print("Set A :- ",A)
print("Set A :- ",A)
print("\n")
print("\n")

length=len(it_companies)
print("Length of it companies :- ",length)

it_companies.add("Twitter")
elements_it={"it1","it2","it3"}
new=it_companies.union(elements_it)
print("After joining new it companies :- ",new)
it_companies.remove("Apple")
print("New dict after removing :- ",it_companies)


C=A.union(B)
print("A dictionary after joining with B :- ",C)

D=A.intersection(B)
print("Intersection between A and B :- ",D)

sub_set=A.issubset(B)
print("Is A subset of B :- ",sub_set)

E=A.isdisjoint(B)

print("Is A and B disjoint se ? ",E)

F=A.union(B)
f2=B.union(A)
print("A join with B :- ",F)
print("B join with A :- ",f2)

print(A.symmetric_difference(B))

#deleting sets A and B
del(A)
del(B)

new_age=set(age)

print("Length of age in list :- ",len(age))
print("Length of age in dict :- ",len(new_age))


#comparing the length.....
if len(age) > len(new_age):
    print('Length of age in list is bigger by ',len(age)-len(new_age))
else:
    print('Length of age in dict is bigger by ',len(new_age)-len(age))


string="\t\t**STRING**\n\ni. String is immutable.\nii. String are written in single or double quotes\nExample :- name='Shivam'"

lst="\t\t**LIST**\n\ni. List is mutable.\nii. List consumes more memory.\niii. List are written between square brackets [ ].\nExample :- [1,2,3,4,'hello']"

tple="\t\t**TUPLE**\n\ni. Tuples are immutable.\nii. Tuples consumes less space the list.\niii. Tuples are written between paranthesis brackets ( ).\nExample :- (1,2,3,4,'hello')"

st="\t\t**SETS**\n\ni. Sets are immutable.\nii. Sets consumes less space the list.\niii. Sets are written between curly braces { }.\nExample :- {1,2,3,4,'hello'}"

total=[string,lst,tple,st]
for j in range(4):
    print("\n")
    print(total[j],end="")
    print("\n")
    for i in range(10):
        print("----",end="")
