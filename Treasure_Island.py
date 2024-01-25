print("""  L|J(_)
       )    | (")      (
       ,(.  |`/ \- y  (,`)
      )' (' | \ /\/  ) (.
     (' ),) | _W_   (,)' ).""")


print("👹 Welcome to Treasure Island.👹")
print("🏴‍☠️ Your mission is to find the treasure.🏴‍☠️")

user = input('Your\'re at a crossroad, where do you want to go? Type "Left" Or "Right?"\n').lower()

if user == "right":
    print("Fall into the Hole. Game Over!")
elif user == "left":

    user1 = input("Swim Or Wait!\n").lower()

    if user1 == "swim":
        print("Attacked by trout. Game Over!")
    elif user1 == "wait":
        print("You chose wisely. You've reached the next stage.")

        user2 = input("Which Door? Red or Blue or ... (Fill to Win)\n").lower()

        if user2 == "red":
            print("Burned By Fire! Game Over!")
        elif user2 == "blue":
            print("Eaten by Beasts. Game Over!")
        elif user2 == "win":
            print("Congratulations! You Win! 💍")
        else:
            print("Invalid choice. Game Over!")
    else:
        print("Invalid choice. Game Over!")
else:
    print("Invalid choice. Game Over!")