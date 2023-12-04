#Guess Number Game 

secrete_number = 9 
guess_limit = 3 
count = 0 
while count < guess_limit:
    guess_number = int(input('Guess: '))
    count += 1 
    if guess_number == secrete_number:
        print('You Won')
        break
else:
    print('You Lose!!')