import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from maze import Maze
from player import Player
import random

# Constants
TILE_SIZE = 40
ROWS, COLS = 10, 10
WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (180, 180, 180)

def draw_maze(screen, maze, player, path):
    for i in range(maze.rows):
        for j in range(maze.cols):
            x = j * TILE_SIZE
            y = i * TILE_SIZE
            tile = maze.grid[i][j]

            if (i, j) == player.position:
                pygame.draw.rect(screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE))
            # elif (i, j) in path and tile == ' ':
            #     pygame.draw.rect(screen, (144, 238, 144), (x, y, TILE_SIZE, TILE_SIZE))  # light green
            elif (i, j) in maze.treasures:
                pygame.draw.rect(screen, (255, 215, 0), (x, y, TILE_SIZE, TILE_SIZE))  # gold color
            elif tile == '#':
                pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 'S':
                pygame.draw.rect(screen, GREEN, (x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 'E':
                pygame.draw.rect(screen, RED, (x, y, TILE_SIZE, TILE_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE), 1)

game_won = False
win_time = None


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Escape")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 24)
    start_ticks = pygame.time.get_ticks()


    maze = Maze(ROWS, COLS)
    player = Player(maze.start_pos)
    # shortest_path = maze.find_shortest_path()

    running = True
    game_won = False
    win_time = None
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and not game_won:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.move('w', maze)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.move('s', maze)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.move('a', maze)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.move('d', maze)
                

        # Timer logic moved up
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        elapsed_sec = elapsed_ms // 1000
        minutes = elapsed_sec // 60
        seconds = elapsed_sec % 60

        draw_maze(screen, maze, player, [])

        if player.position == maze.end_pos and not game_won:
            game_won = True
            win_time = pygame.time.get_ticks()
            pygame.display.set_caption(
                f"🎉 You Escaped this maze!"
            )
        

        # Render the timer
        time_text = f"⏱️ {minutes:02}:{seconds:02}"
        text_surface = font.render(time_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

        treasure_text = f"💎 {player.treasure_collected}"
        treasure_surface = font.render(treasure_text, True, (0, 0, 0))
        screen.blit(treasure_surface, (10, 40))

        pygame.display.flip()

        if game_won:
        # 🎉 Confetti
            for _ in range(100):
                x = random.randint(0, WIDTH)
                y = random.randint(0, HEIGHT)
                size = random.randint(4, 8)
                color = [random.randint(100, 255) for _ in range(3)]
                pygame.draw.rect(screen, color, (x, y, size, size))

            # 🎊 Victory text
            win_text = font.render("🎉 YOU ESCAPED! 🎉", True, (0, 200, 0))
            screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))

    pygame.quit()

    if game_won and pygame.time.get_ticks() - win_time > 5000:
        running = False


if __name__ == "__main__":
    main()
