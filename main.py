from math import sqrt
from random import randint

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)
player_x = 0
player_y = 0
player_found_key = False
steps = 0
distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

print('Find the key! You can move in the following ways: W - up, S - down, A - left, D - right. Type q to quit the game')

while not player_found_key:
    steps += 1
    player_move = input('Where do you go? ')

    match player_move.lower():
        case 'w':
            player_y += 1
            if player_y >= GAME_HEIGHT:
                player_y = GAME_HEIGHT
        case 's':
            player_y -= 1
            if player_y <= 0:
                player_y = 0
        case 'a':
            player_x -= 1
            if player_x <= 0:
                player_x = 0
        case 'd':
            player_x += 1
            if player_x >= GAME_WIDTH:
                player_x = GAME_WIDTH
        case 'q':
            print('Thank you for playing.')
            quit()
        case other:
            print('I can\'t go there.')

    if player_x == key_x and player_y == key_y:
        print('Congratulations, you have found the key!')
        print(f'You have found the key in {steps} moves.')
        quit()

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move < distance_after_move:
        print('Colder')
    else:
        print('Warmer')

    distance_before_move = distance_after_move

