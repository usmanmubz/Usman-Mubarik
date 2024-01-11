import pygame
import sys
import random
import time

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Speed Test")

# Assign colours to named variable
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Add BG
background_image = pygame.image.load("typingtestbackground.jpg").convert()

# Read words from the text file
def read_word_bank(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Text variables
word_list_path = "words_alpha.txt"  # Adding words from file
word_list = read_word_bank(word_list_path)
current_words = random.sample(word_list, 5)  # Pick 5 random words
current_word_index = 0
current_word = current_words[current_word_index]
input_text = ""
start_time = 0
game_active = True

# Additional text
game_title_text = font.render("Typing Speed Test game", True, YELLOW)
made_by_text = font.render("Made by Usman", True, YELLOW)

def draw_text(text, color, y_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

def main():
    global current_words, current_word_index, current_word, input_text, start_time, game_active

    clock = pygame.time.Clock()

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == current_word:
                        current_word_index += 1
                        if current_word_index < len(current_words):
                            current_word = current_words[current_word_index]
                            input_text = ""
                        else:
                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            letters_per_second = len("".join(current_words)) / elapsed_time
                            draw_text(f"Your typing speed: {letters_per_second:.2f} letters per second", YELLOW) # Allow to 2 D.P
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            game_active = False
                    else:
                        input_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Draw background image
        screen.blit(background_image, (0, 0))

        # Draw additional text in the top left corner
        screen.blit(game_title_text, (10, 10))
        screen.blit(made_by_text, (10, 50))

        draw_text(current_word, YELLOW, -50)  # Set font color to yellow
        draw_text(input_text, YELLOW, 50)  # Set font color to yellow

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    start_time = time.time()
    main()

# END OF CODE
