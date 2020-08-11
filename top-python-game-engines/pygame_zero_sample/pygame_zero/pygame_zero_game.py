"""
Simple game in Pygame Zero

This game demonstrates some of the more advanced features of
Pygame Zero, including:
- using sprites to render complex graphics
- handling user input
- sound output

"""

# Import pgzrun allows the program to run in Python IDLE
# You can also run the program from the command line using:
#   `pgzrun pygame_zero_basic.py`
import pgzrun
from typing import Tuple

# To randomize coin placement
from random import randint

# Set the width and height of our output window, in pixels
WIDTH = 800
HEIGHT = 600

# Setup the player
player = Actor("alien_green_stand")
player_position = WIDTH // 2, HEIGHT // 2
player.center = player_position

# Setup the coins to collect
COIN_COUNT = 10
coin_list = list()

# Setup a timer to create new coins
coin_countdown = 2.5
coin_interval = 0.1

# Score is initially zero
score = 0


def add_coin():
    """Adds a new coin to playfield, then
    schedules the next coin to be added
    """
    global coin_list, coin_countdown

    # Create a new coin Actor at a random location
    new_coin = Actor(
        "coin_gold", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10))
    )

    # Add it to the global coin list
    coin_list.append(new_coin)

    # Decrease the time between coin appearances if there are
    # less than three coins on the screen.
    if len(coin_list) < 3:
        coin_countdown -= coin_interval

    # Make sure we don't go too fast
    if coin_countdown < 0.1:
        coin_countdown = 0.1

    # Schedule the next coin addition
    clock.schedule(add_coin, coin_countdown)


def on_mouse_move(pos: Tuple):
    """Called whenever the mouse changes position
    
    Arguments:
        pos {Tuple} -- The current position of the mouse
    """
    global player_position

    # Set the player to the mouse position
    player_position = pos

    # Ensure the player doesn't move off the screen
    if player_position[0] < 0:
        player_position[0] = 0
    if player_position[0] > WIDTH:
        player_position[0] = WIDTH

    if player_position[1] < 0:
        player_position[1] = 0
    if player_position[1] > HEIGHT:
        player_position[1] = HEIGHT


def update(delta_time: float):
    """Called every frame to update game objects
    
    Arguments:
        delta_time {float} -- Time since the last frame
    """
    global coin_list, score

    # Update the player position
    player.center = player_position

    # Check if the player has collided with a coin
    # First, setup a list of coins to remove
    coin_remove_list = []

    # Check each coin in the list for a collision
    for coin in coin_list:
        if player.colliderect(coin):
            sounds.coin_pickup.play()]
            coin_remove_list.append(coin)
            score += 10

    # Remove any coins with which we collided
    for coin in coin_remove_list:
        coin_list.remove(coin)

    # The game is over when there are too many coins on the screen
    if len(coin_list) >= COIN_COUNT:
        # Stop making new coins
        clock.unschedule(add_coin)

        # Print the final score and exit the game
        print(f"Game over! Final score: {score}")
        exit()


def draw():
    """Render everything on the screen once per frame"""

    # Clear the screen first
    screen.clear()

    # Set the background color to pink
    screen.fill("pink")

    # Draw the player
    player.draw()

    # Draw the remaining coins
    for coin in coin_list:
        coin.draw()

    # Draw the current score at the bottom
    screen.draw.text(
        f"Score: {score}", (50, HEIGHT - 50), fontsize=48, color="black",
    )


# Schedule the first coin to appear
clock.schedule(add_coin, coin_countdown)

# Run the program
pgzrun.go()
