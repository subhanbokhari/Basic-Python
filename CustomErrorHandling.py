a = int(input("Enter a value between 5 and 10: "))

if(a < 5 or a > 10):
    raise ValueError("Invalid bounds must be between 5 and 10")


