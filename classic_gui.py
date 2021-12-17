print("welcome")
i=1
while(i>0):
    print("Main menu")
    print("1. calculator")
    print("2. area finder")
    print("3. volume finder")
    print("4. exit")
    opt=int(input("choose any option"))
    if(opt==1):
        print("you choose calculator")
        print("which type of calculation you want: ")
        print("1. Addition")
        print("2. substraction")
        print("3. multiplication")
        print("4. divide")
        answer=int(input("choose any option"))
        if(answer==1):
            num1=int(input("Enter number 1: "))
            num2=int(input("Enter number 2: "))
            add=num1+num2
            print("your ADDITION answer: ",add)
        elif(answer==2):
            num1=int(input("Enter number 1: "))
            num2=int(input("Enter number 2: "))
            sub=num1-num2
            print("your substraction answer: ",sub)
        elif(answer==3):
            num1=int(input("Enter number 1: "))
            num2=int(input("Enter number 2: "))
            mul=num1*num2
            print("your multiplication answer: ",mul)
        elif(answer==4):
            num1=int(input("Enter number 1: "))
            num2=int(input("Enter number 2: "))
            divide=num1/num2
            print("your division answer: ",divide)
        print("do you want to return main menu")
        answer=input("yes/no")
        if(answer=="yes"):
            print("go ahead")
            continue
        else:
            break
    elif(opt==2):
        print("you choose area finder")
        print("which shape of area you want: ")
        print("1. square")
        print("2. rectangle")
        print("3. circle")
        print("4. triangle")
        answer=int(input("choose any option"))

        if(answer==1):
            side=int(input("Enter side: "))
            area=side**2
            print("area of square answer: ",area)
        elif(answer==2):
            l=int(input("Enter number 1: "))
            b=int(input("Enter number 2: "))
            area=l*b
            print("area of rectangle: ",area)
        elif(answer==3):
            r=int(input("Enter radius: "))
            pi=3.14
            area=pi*(r**2)
            print("area of circle",area)
        elif(answer==4):
            base=int(input("Enter base: "))
            height=int(input("Enter height: "))
            area=0.5*base*height
            print("are of triangle: ",area)
        print("do you want to return main menu")
        answer=input("yes/no")
        if(answer=="yes"):
            print("go ahead")
            continue
        else:
            break
    elif(opt==3):
        print("you choose volume finder")
        print("which shape of volume you want: ")
        print("1. sphere")
        print("2. cylinder")
        print("3. cone")
        answer=int(input("choose any option"))
        
        if(answer==1):
            r=int(input("Enter radius: "))
            pi=3.14
            volume=(4/3)*pi*(r**3)
            print("volume of circle",volume)
        elif(answer==2):
            r=int(input("Enter radius: "))
            h=int(input("Enter height 2: "))
            volume=3.14*(r**2)*h
            print("volume of rectangle: ",volume)
        elif(answer==3):
            r=int(input("Enter radius: "))
            h=int(input("Enter height 2: "))
            volume=(1/3)*3.14*(r**2)*h
            print("volume of rectangle: ",volume)
        print("do you want to return main menu")
        answer=input("yes/no")
        if(answer=="yes"):
            print("go ahead")
            continue
        else:
            break
    else:
        break
    i+=1
        
            
