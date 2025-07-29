print("Welcome to the rollercoaster!")
height = int(input("what is your height in cms: "))

if height >= 120:
    print("You can ride rollercoaster")
    age = int(input("what is your age: "))
    if age <= 12:
        print("You have to pay $5")
        
    elif age <= 18:
        print("You have to pay $10")
        
    else:  
         print("You have to pay $15")   
else:
    print("You can't ride rollercoaster")