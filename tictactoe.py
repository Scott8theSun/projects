# This creates a simple grid using Pygame that allows the user to click on the grid
# to place a marker; mimicking the game "Tic Tac Toe"

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 50
HEIGHT = 50

# This sets the margin between each cell
MARGIN = 5

# Initialize counters for players win
player1_win = 0
player2_win = 0

# Create a 2 dimensional array; a list of lists
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(3):
    # Add an empty array that will hold each cell in this row
    grid.append([])
    for column in range(3):
        grid[row].append(0)  # Append a cell

# Initialize pygame and font
pygame.init()
pygame.font.init()
font_game = pygame.font.SysFont("Arial", 20)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Tic Tac Toe")

# Initialize game state
game_over = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set the current player (X goes first)
player1_turn = True


# Check who wins
def check_win(grid):
    # Check if player 1 has won
    for row in range(3):
        if grid[row][0] == "X" and grid[row][1] == "X" and grid[row][2] == "X":
            return 1

    for column in range(3):
        if grid[0][column] == "X" and grid[1][column] == "X" and grid[2][column] == "X":
            return 1

    if grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        return 1

    if grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        return 1

    # Check if player 2 has won
    for row in range(3):
        if grid[row][0] == "O" and grid[row][1] == "O" and grid[row][2] == "O":
            return 2

    for column in range(3):
        if grid[0][column] == "O" and grid[1][column] == "O" and grid[2][column] == "O":
            return 2

    if grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        return 2

    if grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        return 2

    # If no player has won, return 0
    return 0


# Main Program Loop
while not game_over:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_over = True  # Flag that we are done so we exit this loop
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to the current player
            if grid[row][column] != 0:
                continue
            # Switch current player
            if player1_turn:
                grid[row][column] = "X"
            else:
                grid[row][column] = "O"

            player1_turn = not player1_turn

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(3):
        for column in range(3):
            color = WHITE
            if grid[row][column] == "X":
                color = GREEN
            elif grid[row][column] == "O":
                color = RED
            pygame.draw.rect(
                screen,
                color,
                [
                    (MARGIN + WIDTH) * column + MARGIN,
                    (MARGIN + HEIGHT) * row + MARGIN,
                    WIDTH,
                    HEIGHT,
                ],
            )

    # Check if a player has won
    winner = check_win(grid)
    if winner != 0:
        # Update win counter for winner
        if winner == 1:
            player1_win += 1
            grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Reset the board
        else:
            player2_win += 1
            grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    else:
        # Check if game is tied
        tied = True
        for row in range(3):
            for column in range(3):
                if grid[row][column] == 0:
                    tied = False
                    break
            if not tied:
                break
        if tied:
            # Reset game
            grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        game_over = False

    # Draw score board and reset the game
    player1_text = pygame.font.Font.render(font_game, "Player 1 wins: " + str(player1_win), True, GREEN)
    screen.blit(player1_text, [10, 180])
    player2_text = pygame.font.Font.render(font_game, "Player 2 wins: " + str(player2_win), True, RED)
    screen.blit(player2_text, [10, 200])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


