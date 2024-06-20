x = int(input("Input the number: "))

match x:
    
    case 1:
        print("correct perfect")
    case _ if(x>1 and x<10):
        print("correct very close")
    case _ if(x>25 and x<34):
        print("correct near")
    case 4:
        print("correct")
    case _:
        print("Wrong")
