import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Islamic Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Fonts
font = pygame.font.SysFont("Arial", 28)

# ---------------- CLASSES ----------------
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, choice):
        return choice == self.correct_answer


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1

    def update_score(self, points):
        self.score += points

    def advance_level(self):
        self.level += 1


class QuizGame:
    def __init__(self, player, levels):
        self.player = player
        self.levels = levels
        self.current_level = 1
        self.current_index = 0
        self.questions = self.levels[self.current_level]

    def current_question(self):
        return self.questions[self.current_index]

    def next_question(self):
        self.current_index += 1
        if self.current_index >= len(self.questions):
            return False
        return True

    def draw_question(self, question):
        screen.fill(WHITE)
        # Display question
        text_surface = font.render(question.text, True, BLACK)
        screen.blit(text_surface, (50, 50))

        # Display options
        for i, option in enumerate(question.options):
            option_surface = font.render(f"{i+1}. {option}", True, BLACK)
            screen.blit(option_surface, (100, 150 + i*50))

        pygame.display.update()

    def run_level(self):
        running = True
        while running:
            question = self.current_question()
            self.draw_question(question)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        choice = int(event.unicode) - 1
                        if question.is_correct(question.options[choice]):
                            self.player.update_score(10)
                            print("Correct!")
                        else:
                            print("Wrong!")

                        if not self.next_question():
                            running = False

        # Level complete
        screen.fill(WHITE)
        end_text = font.render(f"Level {self.current_level} Complete! Score: {self.player.score}", True, BLACK)
        screen.blit(end_text, (100, 300))
        pygame.display.update()
        pygame.time.wait(2000)

    def run(self):
        for lvl in sorted(self.levels.keys()):
            self.current_level = lvl
            self.questions = self.levels[lvl]
            self.current_index = 0
            self.run_level()

            # Progression check
            if self.player.score < lvl * 20:  # threshold increases with level
                screen.fill(WHITE)
                fail_text = font.render(f"Game Over! You did not qualify for Level {lvl+1}. Final Score: {self.player.score}", True, RED)
                screen.blit(fail_text, (50, 300))
                pygame.display.update()
                pygame.time.wait(3000)
                return

            self.player.advance_level()

        # End screen
        screen.fill(WHITE)
        end_text = font.render(f"Congratulations {self.player.name}! Final Score: {self.player.score}", True, GREEN)
        screen.blit(end_text, (100, 300))
        pygame.display.update()
        pygame.time.wait(3000)


# ---------------- QUESTIONS ----------------
levels = {
    1: [
        Question("Who was the last Prophet in Islam?", 
                 ["Prophet Musa", "Prophet Isa", "Prophet Muhammad (SAW)", "Prophet Ibrahim"], 
                 "Prophet Muhammad (SAW)"),
        Question("Which city is called the heart of Islam?", 
                 ["Medina", "Mecca", "Jerusalem", "Baghdad"], 
                 "Mecca")
    ],
    2: [
        Question("How many pillars of Islam are there?", 
                 ["3", "4", "5", "6"], 
                 "5"),
        Question("What is the holy book of Islam?", 
                 ["Torah", "Bible", "Quran", "Zabur"], 
                 "Quran")
    ],
    3: [
        Question("Which month do Muslims fast?", 
                 ["Rajab", "Ramadan", "Muharram", "Shaban"], 
                 "Ramadan"),
        Question("Where did the Prophet (SAW) migrate to from Mecca?", 
                 ["Taif", "Medina", "Jerusalem", "Baghdad"], 
                 "Medina")
    ]
}

# ---------------- MAIN ----------------
player = Player("Jannatul")
game = QuizGame(player, levels)
game.run()
