import pygame
import random
import time

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
score = 0
level = 1
speed = 10

# Food generation variables
food = None
food_spawn_time = 0
food_timer = 5  # Food disappears after 5 seconds
food_weight = 0  # The "weight" or value of the food, initially 0

# Function to generate food at a random position
def generate_food():
    empty_spaces = [(x * GRID_SIZE, y * GRID_SIZE) 
                    for x in range(WIDTH // GRID_SIZE) 
                    for y in range(HEIGHT // GRID_SIZE) 
                    if (x * GRID_SIZE, y * GRID_SIZE) not in snake]
    
    # Assign a random weight to the food between 1 and 3
    weight = random.randint(1, 3)
    
    if empty_spaces:
        new_food = random.choice(empty_spaces)
        return new_food, weight
    return None, 0

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
        score += food_weight  # Increase score by food's weight
        food = None  # Remove the food after it is eaten
        food_spawn_time = time.time()  # Reset the timer for the next food spawn
        food_weight = 0  # Reset food weight after eating
        
        # Level up every 4 food items
        if score % 4 == 0:
            level += 1
            speed += 2  # Increase speed at each level
    else:
        snake.pop()  # Remove last segment to maintain length

    # If food is not on the screen or has disappeared, generate new food
    if food is None or time.time() - food_spawn_time >= food_timer:
        food, food_weight = generate_food()
        food_spawn_time = time.time()  # Reset the spawn timer
    
    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    
    # Draw the food
    if food is not None:
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

pygame.quit()
