def mult(s):
    try:
        for i in range(1,11):
            print(f"{int(s)} x {i} = {int(s)*i}")
    except Exception as e:
        print("Error!",e)
    finally:
        print("I am always executed")

s = input("Enter the Number: ")
print(f"Multiplication Table of {s}")


mult(s)