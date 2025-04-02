import pygame
import math

pygame.init()

# Constants
fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0  # Default shape (circle)
active_color = 'white'

# Pygame screen setup
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []

# Function to draw the menu bar
def draw_menu(color):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])  # Menu background
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    
    # Brush selection buttons
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20, 2)
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)
    
    # Additional shape selection
    square_brush = [pygame.draw.rect(screen, 'black', [130, 10, 50, 50]), 2]
    pygame.draw.rect(screen, 'white', [135, 15, 40, 40], 2)
    right_triangle_brush = [pygame.draw.rect(screen, 'black', [190, 10, 50, 50]), 3]
    pygame.draw.polygon(screen, 'white', [(195, 55), (240, 55), (195, 15)], 2)
    equilateral_triangle_brush = [pygame.draw.rect(screen, 'black', [250, 10, 50, 50]), 4]
    pygame.draw.polygon(screen, 'white', [(255, 55), (295, 55), (275, 15)], 2)
    rhombus_brush = [pygame.draw.rect(screen, 'black', [310, 10, 50, 50]), 5]
    pygame.draw.polygon(screen, 'white', [(335, 10), (360, 35), (335, 60), (310, 35)], 2)
    
    brush_list = [circle_brush, rect_brush, square_brush, right_triangle_brush, equilateral_triangle_brush, rhombus_brush]
    
    # Color selection
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)
    
    # Color options
    colors = [
        pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25]),  # Blue
        pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25]),  # Red
        pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25]),  # Green
        pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25]),  # Yellow
        pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25]),  # Teal
        pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25]),  # Purple
        pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25]),  # Black
        pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])  # White
    ]
    
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]
    
    return brush_list, colors, rgb_list

# Function to draw the painting
def draw_painting(paints):
    for color, pos, figure in paints:
        if figure == 0:
            pygame.draw.circle(screen, color, pos, 20, 2)
        elif figure == 1:
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)
        elif figure == 2:
            pygame.draw.rect(screen, color, [pos[0] - 20, pos[1] - 20, 40, 40], 2)  # Square
        elif figure == 3:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] - 20, pos[1] + 20), (pos[0] + 20, pos[1] + 20)], 2)  # Right Triangle
        elif figure == 4:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] - 20, pos[1] + 20), (pos[0] + 20, pos[1] + 20)], 2)  # Equilateral Triangle
        elif figure == 5:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] + 20, pos[1]), (pos[0], pos[1] + 20), (pos[0] - 20, pos[1])], 2)  # Rhombus

# Main loop
run = True
brushes, colors, rgbs = draw_menu(active_color)
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    brushes, colors, rgbs = draw_menu(active_color)

    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure))
    draw_painting(painting)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]
    
    pygame.display.flip()
pygame.quit()
