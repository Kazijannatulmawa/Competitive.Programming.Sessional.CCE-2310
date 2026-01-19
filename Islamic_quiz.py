import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup with dimensions
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Islamic Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (180, 180, 180)

# Fonts
font = pygame.font.SysFont("Arial", 32)

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

        # Display options as buttons
        self.buttons = []
        for i, option in enumerate(question.options):
            rect = pygame.Rect(100, 150 + i*80, 600, 60)
            pygame.draw.rect(screen, GRAY, rect)
            option_surface = font.render(option, True, BLACK)
            screen.blit(option_surface, (120, 160 + i*80))
            self.buttons.append((rect, option))

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for rect, option in self.buttons:
                        if rect.collidepoint(mouse_pos):
                            if question.is_correct(option):
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
            random.shuffle(self.questions)  # shuffle questions each level
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


# ---------------- QUESTION BANK ----------------
levels = {
    1: [
        Question("Who was the last Prophet in Islam?", 
                 ["Prophet Musa", "Prophet Isa", "Prophet Muhammad (SAW)", "Prophet Ibrahim"], 
                 "Prophet Muhammad (SAW)"),
        Question("Which city is called the heart of Islam?", 
                 ["Medina", "Mecca", "Jerusalem", "Baghdad"], 
                 "Mecca"),
        Question("How many pillars of Islam are there?", 
                 ["3", "4", "5", "6"], 
                 "5"),
        Question("What is the holy book of Islam?", 
                 ["Torah", "Bible", "Quran", "Zabur"], 
                 "Quran")
    ],
    2: [
        Question("Which month do Muslims fast?", 
                 ["Rajab", "Ramadan", "Muharram", "Shaban"], 
                 "Ramadan"),
        Question("Where did the Prophet (SAW) migrate to from Mecca?", 
                 ["Taif", "Medina", "Jerusalem", "Baghdad"], 
                 "Medina"),
        Question("What is the first pillar of Islam?", 
                 ["Shahada", "Salah", "Zakat", "Hajj"], 
                 "Shahada"),
        Question("How many daily prayers are obligatory?", 
                 ["3", "4", "5", "6"], 
                 "5")
    ],
    3: [
        Question("Which angel brought revelation to the Prophet (SAW)?", 
                 ["Mikail", "Israfil", "Jibreel", "Azrael"], 
                 "Jibreel"),
        Question("What is the pilgrimage to Mecca called?", 
                 ["Umrah", "Hajj", "Tawaf", "Salah"], 
                 "Hajj"),
        Question("Which battle was the first major battle in Islam?", 
                 ["Battle of Uhud", "Battle of Badr", "Battle of Khandaq", "Battle of Hunayn"], 
                 "Battle of Badr"),
        Question("What is the night of power in Ramadan called?", 
                 ["Laylat al-Qadr", "Laylat al-Miraj", "Laylat al-Baraat", "Laylat al-Isra"], 
                 "Laylat al-Qadr")
    ]
}

# ---------------- MAIN ----------------
player = Player("Jannatul")
game = QuizGame(player, levels)
game.run()

