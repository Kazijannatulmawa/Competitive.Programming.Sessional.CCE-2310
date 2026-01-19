#Snake Game By Mawa
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
#BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
#GREEN = (0, 255, 0)
#RED = (255, 0, 0)
DARK_GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
DARK_GRAY = (20, 20, 20)
GRID_COLOR = (30, 30, 30)
SNAKE_HEAD = (50, 200, 50)
SNAKE_BODY = (34, 139, 34)
SNAKE_OUTLINE = (25, 100, 25)
FOOD_RED = (220, 20, 60)
FOOD_HIGHLIGHT = (255, 69, 96)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body = [(start_x - i, start_y) for i in range(5)]  # Snake starts with 5 segments
        self.direction = RIGHT
        self.grow = False
    
    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_direction):
        # Prevent moving in opposite direction
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def check_collision(self):
        head = self.body[0]
        # Check wall collision
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        # Check self collision
        if head in self.body[1:]:
            return True
        return False
    
    def eat_food(self, food_pos):
        if self.body[0] == food_pos:
            self.grow = True
            return True
        return False

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)
    
    def generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body:
                return pos

def draw_grid(screen):
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

            
def draw_background(screen):
    screen.fill((34, 139, 34))  # base green
    for i in range(0, WINDOW_WIDTH, GRID_SIZE):
        for j in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.rect(screen, (30, 120, 30), (i, j, GRID_SIZE, GRID_SIZE), 1)

def draw_snake(screen, snake):
    for i, (x, y) in enumerate(snake.body):
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)

        if i == 0:  # Head
            pygame.draw.ellipse(screen, (139, 69, 19), rect)  # SaddleBrown head
            pygame.draw.ellipse(screen, (100, 50, 20), rect, 2)  # Outline

            # Eyes
            eye_radius = 3
            eye_offset_x = 5
            eye_offset_y = 5
            pygame.draw.circle(screen, WHITE, (rect.centerx - eye_offset_x, rect.centery - eye_offset_y), eye_radius)
            pygame.draw.circle(screen, WHITE, (rect.centerx + eye_offset_x, rect.centery - eye_offset_y), eye_radius)

            # Tongue
            tongue_start = (rect.centerx, rect.centery + 5)
            tongue_end = (rect.centerx, rect.centery + 12)
            pygame.draw.line(screen, (255, 0, 0), tongue_start, tongue_end, 2)

        else:  # Body
            pygame.draw.ellipse(screen, (160, 82, 45), rect)  # Sienna body
            pygame.draw.ellipse(screen, (100, 50, 20), rect, 1)  # Outline

def draw_food(screen, food):
    x, y = food.position
    rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.circle(screen, (220, 20, 60), rect.center, GRID_SIZE // 2)  # apple
    pygame.draw.line(screen, (0, 150, 0), rect.center, (rect.centerx, rect.centery - 8), 2)  # stem

def draw_score(screen, score, font):
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over_screen(screen, score, font):
    screen.fill(BLACK)
    game_over_text = font.render('GAME OVER!', True, RED)
    score_text = font.render(f'Final Score: {score}', True, WHITE)
    restart_text = font.render('Press SPACE to restart or ESC to quit', True, WHITE)
    
    screen.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 60))
    screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, WINDOW_HEIGHT // 2))
    screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 + 60))
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    while True:
        # Initialize game
        snake = Snake()
        food = Food(snake.body)
        score = 0
        game_active = True
        paused = False
        
        
        while game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(RIGHT)
                    elif event.key == pygame.K_p:  # Pause toggle
                        paused = not paused    
            if not paused:

                # Move snake
                snake.move()
            
                # Check collisions
                if snake.check_collision():
                    game_active = False
                    continue
            
                # Check if food eaten
                if snake.eat_food(food.position):
                    score += 1
                    food = Food(snake.body)
            
            # Draw everything
            screen.fill(BLACK)
            draw_grid(screen)
            draw_background(screen)
            draw_snake(screen, snake)
            draw_food(screen, food)
            draw_score(screen, score, font)
            if paused:
                 # Draw pause overlay
                 pause_text = font.render("PAUSED", True, YELLOW)
                 sub_text = font.render("Press P to Resume", True, WHITE)

                 screen.blit(pause_text, (WINDOW_WIDTH // 2 - pause_text.get_width() // 2,
                             WINDOW_HEIGHT // 2 - pause_text.get_height() // 2 - 20))
                 screen.blit(sub_text, (WINDOW_WIDTH // 2 - sub_text.get_width() // 2,
                           WINDOW_HEIGHT // 2 - sub_text.get_height() // 2 + 20))
            
            pygame.display.flip()
            clock.tick(10)  # Game speed
        
        # Game over screen
        game_over_screen(screen, score, font)
        
        # Wait for restart or quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

if __name__ == '__main__':
    main()