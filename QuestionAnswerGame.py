answers = ["Subhan", "Peshawar", "Islamabad", "K2", "Abu Dhabi"]

a1 = input("What is the name of the organizer? For 25 Lakhs! ")

k = 0

if a1 == answers[0]:
    print("Correct! 25 Lakhs")
    k = 25
else:
    print("You Lost all")

if k == 25:
    t = input("Will you like to Risk it for 50 Lakhs?")
    if t.lower() == "yes":
        a2 = input("City which he is in currently? ")
        if a2 == answers[1]:
            print("Correct! 50 Lakhs")
            k = 50
        else:
            print("You Lost all")
            k = 0

if k == 50:
    t1 = input("Will you like to Risk it for 75 Lakhs?")
    if t1.lower() == "yes":
        a3 = input("What is the capital of Pakistan? ")
        if a3 == answers[2]:
            print("Correct! 75 Lakhs")
            k = 75
        else:
            print("You Lost all")
            k = 0

if k == 75:
    t1 = input("Will you like to Risk it for 1 Crores?")
    if t1.lower() == "yes":
        a3 = input("What is the second highest peak in the world? ")
        if a3 == answers[3]:
            print("Correct! 1 Crores")
            k = 100
        else:
            print("You Lost all")
            k = 0

if k == 100:
    t1 = input("Will you like to Risk it for 1.25 Crores?")
    if t1.lower() == "yes":
        a4 = input("What is the capital of UAE? ")
        if a4 == answers[4]:
            print("Correct! 1.25 Crores")
            k = 125
        else:
            print("You Lost all")
            k = 0

if k == 25:
    print("You won 25 lakhs!")
elif k == 50:
    print("You won 50 lakhs!")
elif k == 75:
    print("You won 75 lakhs!")
elif k == 100:
    print("You won 1 Crore!")
elif k == 125:
    print("You won 1.25 Crores!")
elif k == 0:
    print("Don't be greedy sometimes!")