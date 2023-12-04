#Car Engine Game Start Stop 

print('To the Game: Start, Stop, Quit, Help')
command = ''

while True:  
    command = input('> ').lower()
    if command == 'start':
        print('Car Started...Ready to go!')
    elif command =='stop':
        print('Car stopped')
    elif command == 'help':
        print('''
Start - to start the car
Stop - to stop the car
Quit - to quit
''')
    elif command =='quit':
        break
    else:
        print('Sorry, I dont understand it')