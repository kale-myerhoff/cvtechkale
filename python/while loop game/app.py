from random import randint

secret_number = randint(1, 100)
guess_count = 1
guess_limit = 10
while guess_count <= guess_limit:
    try:
        guess = int( input(f'{guess_count}/{guess_limit} guess: '))
        guess_count +=1
        if guess == secret_number:
            print (f"you won, the number was {secret_number}!! :D")
            break
        elif guess > secret_number:
            print("too high")
        elif guess < secret_number:
            print("too low")
    except ValueError:
        print('Number please :D')
else:
    print(f'you lost the number was {secret_number} :(')