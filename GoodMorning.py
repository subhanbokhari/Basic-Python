''' 
 Create a python program capable of greeting you with Good Morning, 
 Good Afternoon and Good Evening. 
 Your program should use time module to get the current hour. 
'''
import time

now = time.localtime()
now_time = int(time.strftime("%H"))

print(now_time)

if(now_time >= 0 and now_time < 12):
    print("Good Morning!")
    
if(now_time >= 12 and now_time < 18):
    print("Good Afternoon!")
    
if(now_time >= 18 and now_time < 24):
    print("Good Evening!")

  