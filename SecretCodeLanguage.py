import random
import string

print("Welcome to the Portal")
a = int(input("How can we help you today? 1.Encode 2.Decode? "))

if a == 1:
    s = input("Please input the word: ")
    print("Starting Encoding...")
    if len(s) > 3:
        s = s + s[0]
        new_s = s[1:len(s)]
        print(new_s)
        rand = random.choices(string.ascii_letters, k=3)
        new_s = new_s + rand[0] + rand[1] + rand[2]

        new_2_s = ''.join(rand) + new_s
        print(new_2_s)
    elif len(s) < 3:
        p = s[::-1]
        print(p)

if a == 2:
    t = input("Please Enter the Message: ")
    print("Decoding...")
    new_t = t[3:len(t)-3]
    d = t[0]
    final = d + new_t
    print(final)