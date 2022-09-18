import os
import random
import time
for i in range (1000000):
    os.system("clear")
    table = int(input("what table do you want 2 or 3? "))
    if table == 2:
        number = random.randrange(1, 10)
        question = str("2 x " + str(number) + " =? ")
        result = int(input(question))
        if result == 2 * number:
            print ("Correct")
        else:
            print("Wrooooong")
            
    if table == 3:        
        number = random.randrange(1, 10)
        question = str("3 x " + str(number) + " =? ")
        result = int(input(question))
        if result == 3 * number:
            print ("Correct")
        else:
            print("Wrooooong")
            
            
            
            
    time.sleep(2)