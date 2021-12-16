print("WELCOME TO SAITM")
i=1
password=6733
money=3400000
while(i>0):
    print("1. withdrawl")
    print("2. update password")
    user=int(input("CHOOSE ANY OF THEM: "))
    
    if(user==1):
        password=int(input("enter your password: "))
        if(password==6733):
            print("you choose withdrawl")
            withdraw=int(input("how much you want to withdraw"))
            if(money>=withdraw):
                left=money-withdraw
                print("you entered amount ",withdraw," from your account")
                print("please collect your money")
                answer=input("do you want to see your balance")
            else:
                print("you have insufficient balance")
                continue
            if(answer=="yes"):
                print(left)
            elif(answer=="no"):
                print("thank you")
        else:
            print("wrong password")
            
    elif(user==2):
        password=int(input("enter your password"))
        if(password==6733):
            print("welcome to updation part")
            print("you want to update password")
            answer=input("enter yes or no")
            if(answer=="yes"):
                password=input("enter your new password: ")
                print("you entered: ",password)
            else:
                print("your password did not matched")
        else:
            print("your password did not matched")
    i+=1      
            
            
        
