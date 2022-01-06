amount= []
ele = int(input("enter your total amount:"))
amount.append(ele)
print("select one of them:")
while(1>0):
    print(" 1. deposite\n","2. withdrawl\n","3. bank summery")
    opt=int(input("choose one of them: "))
    if opt==1:
        print("you choose deposite")
        deposite=int(input("enter the amount you want to deposite"))
        total=amount[-1]+deposite
        amount.append(total)
        print("your new balance is:",total)
    elif opt==2:
        print("you choose withdraw")
        withdraw=int(input("enter the amount you want to withdraw"))
        if withdraw<=ele in amount:
            total=amount[-1]-withdraw
            amount.append(total)
            print("your new balance is:",total)
        else:
            print("insufficient")
    elif opt==3:
        print("your full summery is:")
        for i in amount:
            print(i,end=";")
        print()
    else:
        break




