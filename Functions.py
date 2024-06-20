def tables(num):
    i = 0
    while(i<    11):
        print(num,"x",i, "=",num * i)
        i += 1
        
def square(num):
    print("The Square is: ",num * num)        
        

num = int(input("Input the number for it's Table: "))
tables(num)
square(num)