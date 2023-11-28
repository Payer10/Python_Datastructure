import random as r
secret_age=r.randint(1,10)
flag = False

def game_func(guessed_age,secret):
    if guessed_age < secret:
        return 'Too low'
    elif guessed_age > secret:
        return 'Too high'
    else:
        return 'CORRECT!'

for i in range(1,6):
    print('Take a guess. you have'+str(6-i)+'guesses left')
    guess = input()
    if game_func(int(guess),secret_age) == 'CORRECT!':
        print('YOU HAVE WIN THE GAME')
        flag=True
        break
if not flag:
    print('YOU LOST THE GAME')
      
