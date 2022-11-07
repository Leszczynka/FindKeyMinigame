# Find key - minigame
The player's mission is to find the key randomly placed on the board.

## Table of contents
* [Key features](#key-features)
* [Technology](#technology)
* [Setup](#setup)
* [Ideas for future development](#ideas)

### Key features
Board size: 10 x 10.

Player possible moves:
W - up, S - down, A - left, D - right.

The player gets a hint after each move: warmer or colder - depending on whether the distance between the player's position and the key's position decreases or increases.

After found the key, player receives information on how many moves it took.

### Technology
Python 3.10

In order to implement player movements, I used the new functionality of python version 3.10 - match case statement.

### Setup
Clone or download the repo.

From your command line pointing to the project root directory, type:
```bash
python main.py
```
and ... have fun! :)

### Ideas for feature development
* Possibility to choose the game mode: easy, medium, difficult by implementing different board sizes.
* Create visual interface (GUI).