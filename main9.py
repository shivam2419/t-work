import math

pi=math.pi

pi_str=str(pi)
count=-1

def call():
    
    print(pi_str[count])



while True:
    ask=input("Do you want to call the function \n[y/n] :-")
    if ask=="y" and count<10:
        count+=1
        call()
        if count==10:
            print("Can't do more than 10 times")

    else:
        print(pi_str[0:count])
        print("OKAY !!")
        break
