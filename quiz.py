print("do you want to play game")
ans=input()
points=0
if(ans=="YES" and ans=="yes"):
    print("go ahead")
    print("Q.1= Which of the following is a non metal that remains liquid at room temperature?")
    print("options:")
    print("A.Phosphorous")
    print("B.Bromine")
    print("C.Chlorine")
    print("D.Helium")
    ans1=input("enter your answer: ")
    if(ans1=="B" and ans=="b"):
        print("correct")
        points=points+10
        print("your score: ", points)
    else:
        print("wrong")
        print("your score: ", points)
    print("Q.2= Brass gets discoloured in air because of the presence of which of the following gases in air?")
    print("options:")
    print("A. Oxygen")
    print("B. Hydrogen sulphide")
    print("C. Carbon dioxide")
    print("D. Nitrogen")
    ans2=input("enter your answer: ")
    if(ans2=="B" and ans=="b"):
        print("correct")
        points=points+10
        print("you scored: ", points)
    else:
        print("wrong")
        print("your score: ", points)
    print("Q.3= Chlorophyll is a naturally occurring chelate compound in which central metal is")
    print("options:")
    print("A. copper")
    print("B. magnesium")
    print("C. iron")
    print("D. calcium")
    ans3=input("enter your answer: ")
    if(ans3=="B" and ans=="b"):
        print("correct")
        points=points+10
        print("you scored: ", points)
    else:
        print("wrong")
        print("your score: ", points)
    print("Q.4= Which of the following is used in pencils")
    print("options:")
    print("A. Graphite")
    print("B. Silicon")
    print("C. Charcoal")
    print("D. Phosphorous")
    ans4=input("enter your answer: ")
    if(ans4=="A" and ans=="a"):
        print("correct")
        points=points+10
        print("you scored: ", points)
    else:
        print("wrong")
        print("your score: ", points)
    print("Q.5= Which of the following metals forms an amalgam with other metals?")
    print("options:")
    print("A. Tin")
    print("B. Mercury")
    print("C. Lead")
    print("D. Zinc")
    ans5=input("enter your answer: ")
    if(ans5=="B" and ans=="b"):
        print("correct")
        points=points+10
        print("you scored: ", points)
    else:
        print("wrong")
        print("your score: ", points)
    print("total scored: ", points)   
else:
    print("bye")
print("")





