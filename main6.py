#Thoda different hai try maarna
paragraph='I love teaching.If you do not love teaching what else can you love.I love python if you do not love something which can give you all the capablities to develop an application what else can you love.'

val=[]
for i in paragraph:
    print(i)
    if i==" ":
        continue
    else:
        val.append(i)

new_val=[]
count=0
for i in val:
    if i in new_val:
        count=count+1
        continue
    else:
        new_val.append(i)

print(new_val)

# second question

points=[-4,-3,-1,-1,0,2,4,8]

distance=points[-1]-points[0]
print(distance)