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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)      # Snake Head Color
MAGENTA = (199, 21, 133)    # Snake Body Color
ORANGE = (255, 165, 0)      # Food Color
TEAL = (0, 128, 128)        # Grid Line Color
RED = (255, 0, 0)           # Game Over Text
GRAY = (100, 100, 100)      # Pause Text Color

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, start_pos=(GRID_WIDTH // 2, GRID_HEIGHT // 2)):
        self.body = [start_pos]
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
        # Wall collision
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        # Self collision
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
        pygame.draw.line(screen, TEAL, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, TEAL, (0, y), (WINDOW_WIDTH, y))


def draw_snake(screen, snake):
    SHADOW_COLOR = (70, 0, 70)
    for i, segment in enumerate(snake.body):
        x, y = segment
        color = PURPLE if i == 0 else MAGENTA

        rect_x = x * GRID_SIZE
        rect_y = y * GRID_SIZE
        rect_width = GRID_SIZE - 1
        rect_height = GRID_SIZE - 1

        # Shadow effect
        shadow_offset = 2
        pygame.draw.rect(screen, SHADOW_COLOR,
                         (rect_x + shadow_offset, rect_y + shadow_offset, rect_width, rect_height),
                         border_radius=4)

        # Rounded rectangle
        pygame.draw.rect(screen, color,
                         (rect_x, rect_y, rect_width, rect_height),
                         border_radius=4)


def draw_food(screen, food):
    x, y = food.position
    center_x = x * GRID_SIZE + GRID_SIZE // 2
    center_y = y * GRID_SIZE + GRID_SIZE // 2
    half_size = GRID_SIZE // 2 - 2

    points = [
        (center_x, center_y - half_size),
        (center_x + half_size, center_y),
        (center_x, center_y + half_size),
        (center_x - half_size, center_y)
    ]

    pygame.draw.polygon(screen, ORANGE, points)
    pygame.draw.circle(screen, WHITE, (center_x, center_y), 2)


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


def pause_screen(screen, font):
    pause_text = font.render('PAUSED - Press P to Resume', True, GRAY)
    screen.blit(pause_text, (WINDOW_WIDTH // 2 - pause_text.get_width() // 2, WINDOW_HEIGHT // 2))
    pygame.display.flip()


def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    while True:
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
                    elif event.key == pygame.K_p:
                        paused = not paused

            if paused:
                pause_screen(screen, font)
                clock.tick(5)
                continue

            snake.move()

            if snake.check_collision():
                game_active = False
                continue

            if snake.eat_food(food.position):
                score += 1
                food = Food(snake.body)

            screen.fill(BLACK)
            draw_grid(screen)
            draw_snake(screen, snake)
            draw_food(screen, food)
            draw_score(screen, score, font)

            pygame.display.flip()
            clock.tick(10)

        game_over_screen(screen, score, font)

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