import pygame
import random
import sys
import psycopg2
import time

# Initialize Pygame
pygame.init()

# Database connection
conn = psycopg2.connect(database="abab", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# Define User and User_Score tables
def create_tables():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "User" (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS user_score (
        score_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES "User"(user_id),
        level INT NOT NULL,
        score INT NOT NULL
    );
    """)
    conn.commit()

# Game setup
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

# Functions to handle database interactions
def get_user_id(username):
    cur.execute("SELECT user_id FROM \"User\" WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        cur.execute("INSERT INTO \"User\" (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def insert_user_score(user_id, level, score):
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()

def show_current_level(username):
    cur.execute("""
    SELECT level FROM user_score 
    INNER JOIN "User" ON user_score.user_id = "User".user_id 
    WHERE "User".username = %s ORDER BY score_id DESC LIMIT 1
    """, (username,))
    row = cur.fetchone()
    if row:
        print(f"Welcome back, {username}! Your current level is: {row[0]}")
    else:
        print(f"Welcome, {username}! New player.")

# Snake and Food classes
class Snake:
    # [Class definition unchanged, include here]
    pass

class Food:
    # [Class definition unchanged, include here]
    pass

# Game logic functions
def game_loop(username):
    user_id = get_user_id(username)
    snake = Snake()
    food = Food()
    game_over = False
    game_close = False
    level = 1
    score = 0
    snake_speed = 15

    while not game_over:
        while game_close:
            dis.fill((50, 153, 213))
            message("You lost! Press Q-Quit or C-Play Again", (213, 50, 80))
            show_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop(username)

        # [Include rest of game loop logic here]

def main():
    create_tables()
    username = input("Enter your username: ")
    show_current_level(username)
    game_loop(username)
    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()