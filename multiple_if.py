print("Welcome to the rollercoaster!")
height = int(input("what is your height in cms: "))

if height >= 120:
    print("You can ride rollercoaster")
    age = int(input("what is your age: "))
    if age <= 12:
        bill = 5
        print("You have to pay $5")
        
    elif age <= 18:
        bill = 10
        print("You have to pay $10")
        
    else:  
        print("You have to pay $15")
        bill = 15
    
    wants_picture = input("Do you want to have a picture? Type Y for Yes and N for No. ")
    if wants_picture == "Y":
    # Add $3 to their bill
        bill += 3
        print(f"Your final bill is ${bill}") 
         
    else:
        print(f"Your final bill is ${bill}")      
    
else:
    print("You can't ride rollercoaster")