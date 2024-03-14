# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep
 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# print out some text THIS LINE CAN BE REMOVED 
print('Hello World!\n'*10)
 
# sleep for 2 seconds after printing output. Change the value to a different number for a different time length.
sleep(2)
 
# now call function we defined above
clear()
# The line above can be reused throughout your program to clear the screen. 890-=
