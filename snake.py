import pygame
import time
import random

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Snake segment size
SEGMENT_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for displaying the score
font = pygame.font.SysFont(None, 36)

# Function to display the score on the screen
def display_score(score):
    text = font.render("Score: " + str(score), True, WHITE)
    window.blit(text, (10, 10))

# Function to draw the snake on the screen
def draw_snake(snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], SEGMENT_SIZE, SEGMENT_SIZE))

# Function to generate a random position for the food
def generate_food_position():
    x = random.randint(0, (WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
    y = random.randint(0, (HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
    return x, y

# Main game loop
def game_loop():
    # Initial snake position and direction
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    snake_dx = SEGMENT_SIZE
    snake_dy = 0

    # List to store the snake segments
    snake_segments = []
    snake_length = 1

    # Initial food position
    food_x, food_y = generate_food_position()

    # Game over flag
    game_over = False

    # Score
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_dx != SEGMENT_SIZE:
                    snake_dx = -SEGMENT_SIZE
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT and snake_dx != -SEGMENT_SIZE:
                    snake_dx = SEGMENT_SIZE
                    snake_dy = 0
                elif event.key == pygame.K_UP and snake_dy != SEGMENT_SIZE:
                    snake_dy = -SEGMENT_SIZE
                    snake_dx = 0
                elif event.key == pygame.K_DOWN and snake_dy != -SEGMENT_SIZE:
                    snake_dy = SEGMENT_SIZE
                    snake_dx = 0

        # Update snake position
        snake_x += snake_dx
        snake_y += snake_dy

        # Check for collision with the food
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = generate_food_position()
            snake_length += 1
            score += 10

        # Create a new head segment
        snake_segments.append((snake_x, snake_y))

        # Remove segments if the snake is longer than its length
        if len(snake_segments) > snake_length:
            del snake_segments[0]

        # Check for collision with the boundaries of the window
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            game_over = True

        # Check for collision with the snake's own body
        if (snake_x, snake_y) in snake_segments[:-1]:
            game_over = True

        # Clear the window
        window.fill(BLACK)

        # Draw the snake
        draw_snake(snake_segments)

        # Draw the food
        pygame.draw.rect(window, RED, (food_x, food_y, SEGMENT_SIZE, SEGMENT_SIZE))

        # Display the score
        display_score(score)

        # Update the game display
        pygame.display.update()

        # Set the frame rate
        clock.tick(10)

    # Game over message
    text = font.render("Game Over!", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)

    # Quit Pygame
    pygame.quit()

# Start the game loop
game_loop()
