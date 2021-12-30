from random import randint
again = 'y'
while again == 'y':
    print('Welcome to the Guessing Game!')
    print('Put the two numbers the possible number will be in between')
    num1 = int(input(''))
    num2 = int(input(''))
    number = round(randint(num1, num2))

    possibletries = int(input('How many tries do you want? '))
    x=1
    previousguess = None
    while x <= possibletries:
        guess = int(input("What's your guess? "))
        if guess == number:
            print('You got it!')
            break
        elif not previousguess == None: 
            if abs(previousguess - number) < abs(guess - number):
                print("You're getting colder")
            else:
                print("Wrong, but you're getting warmer!") 
        else:
            print('Wrong')
        previousguess = guess
        x+=1
    if x > possibletries:
        print("Unfortunately, you didn't guess the number " + str(number))
    again = input('Want to do it again? [y/n]')
print('Okay, bye!')