from random import randint

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)
player_x = 0
player_y = 0

player_found_key = False

print('Find the key! You can move in the following ways: W - up, S - down, A - left, D - right. Type q to quit the game')

while not player_found_key:
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
            quit()
        case other:
            print('I can\'t go there.')

    print(player_x, player_y)


