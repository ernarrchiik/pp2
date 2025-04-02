import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SNAKE_COLOR = (0, 200, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake initialization
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_dir = (GRID_SIZE, 0)
food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
        random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
score = 0
level = 1
speed = 10

# Function to generate food at a random position
def generate_food():
    while True:
        new_food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                    random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
        if new_food not in snake:
            return new_food

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Check for wall collision
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False  # Game over if snake hits the wall
    
    # Check for self collision
    if new_head in snake:
        running = False

    # Add new head to the snake
    snake.insert(0, new_head)
    
    # Check if snake eats food
    if new_head == food:
        score += 1
        food = generate_food()
        
        # Level up every 4 food items
        if score % 4 == 0:
            level += 1
            speed += 2  # Increase speed at each level
    else:
        snake.pop()  # Remove last segment to maintain length
    
    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    
    # Draw the food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    
    # Draw score and level
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))
    
    # Refresh screen
    pygame.display.flip()
    clock.tick(speed)

    # Debugging: print game status at each step
    print(f"Snake: {snake}, Food: {food}, Score: {score}, Level: {level}, Speed: {speed}")

pygame.quit()
