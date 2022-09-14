

random_number=87
print(random_number)
i=1
while i<=8:
    user_value=int(input("Enter the number :"))
    if random_number==user_value:
        print(f"You won the game you will take {i}")

        break
    elif user_value  <  random_number:
        print("pls enter the large number")
    elif user_value  >  random_number:
        print("pls enter the small number")

        i=i+1
        print(i)
        if i>8 :
            print("game is over")
    
