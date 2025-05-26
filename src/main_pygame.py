import pygame
import random
import sys

# Symbols for the slot machine
SYMBOLS = ["🍒", "🍋", "🍊", "🍇", "🔔", "7"]
DEFAULT_PROBABILITIES = {
    "🍒": 20,
    "🍋": 20,
    "🍊": 20,
    "🍇": 15,
    "🔔": 15,
    "7": 10
}

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (200, 200, 200)

pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine Simulator")
font = pygame.font.SysFont("Segoe UI Emoji", 64)
small_font = pygame.font.SysFont("Arial", 24)

# Button class
def draw_button(rect, text, color, text_color=BLACK):
    pygame.draw.rect(screen, color, rect)
    label = small_font.render(text, True, text_color)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

def weighted_choice(probabilities):
    symbols = list(probabilities.keys())
    weights = list(probabilities.values())
    return random.choices(symbols, weights=weights, k=1)[0]

def main():
    clock = pygame.time.Clock()
    running = True
    spinning = False
    spin_steps = 0
    max_spin_steps = 10
    result = ["🍒", "🍋", "🍊"]
    probabilities = DEFAULT_PROBABILITIES.copy()
    score = 0
    win_message = ""
    # Button rects
    spin_btn = pygame.Rect(50, 300, 100, 40)
    config_btn = pygame.Rect(250, 300, 100, 40)
    # Config panel state
    config_open = False
    config_inputs = {s: str(probabilities[s]) for s in SYMBOLS}
    input_boxes = []
    active_input = None
    while running:
        screen.fill(WHITE)
        # Draw reels
        for i, symbol in enumerate(result):
            label = font.render(symbol, True, BLACK)
            x = 50 + i * 100
            y = 100
            screen.blit(label, (x, y))
        # Draw result label
        if win_message:
            msg = small_font.render(win_message, True, GREEN)
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, 200))
        # Draw score
        score_label = small_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_label, (WIDTH//2 - score_label.get_width()//2, 250))
        # Draw buttons
        if not config_open:
            draw_button(spin_btn, "Spin", GRAY if spinning else GREEN, WHITE)
            draw_button(config_btn, "Config", GRAY, WHITE)
        # Config panel
        if config_open:
            pygame.draw.rect(screen, GRAY, (30, 60, 340, 260))
            y = 80
            input_boxes = []
            for s in SYMBOLS:
                label = small_font.render(s, True, BLACK)
                screen.blit(label, (60, y))
                box = pygame.Rect(120, y, 40, 32)
                pygame.draw.rect(screen, WHITE, box)
                val = config_inputs[s]
                val_label = small_font.render(val, True, BLACK)
                screen.blit(val_label, (box.x+5, box.y+5))
                input_boxes.append((s, box))
                y += 40
            draw_button(pygame.Rect(200, 220, 80, 32), "Save", GREEN, WHITE)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not config_open and spin_btn.collidepoint(event.pos) and not spinning:
                    spinning = True
                    spin_steps = 0
                    win_message = ""
                elif not config_open and config_btn.collidepoint(event.pos):
                    config_open = True
                    active_input = None
                elif config_open:
                    for s, box in input_boxes:
                        if box.collidepoint(event.pos):
                            active_input = s
                    save_box = pygame.Rect(200, 220, 80, 32)
                    if save_box.collidepoint(event.pos):
                        # Validate and save
                        try:
                            new_probs = {s: int(config_inputs[s]) for s in SYMBOLS}
                        except ValueError:
                            continue
                        if sum(new_probs.values()) == 100:
                            probabilities = new_probs
                            config_open = False
                        else:
                            win_message = "Total must be 100%"
            elif event.type == pygame.KEYDOWN and config_open and active_input:
                if event.key == pygame.K_BACKSPACE:
                    config_inputs[active_input] = config_inputs[active_input][:-1]
                elif event.unicode.isdigit() and len(config_inputs[active_input]) < 3:
                    config_inputs[active_input] += event.unicode
        # Spinning animation
        if spinning:
            if spin_steps < max_spin_steps:
                result = [random.choice(SYMBOLS) for _ in range(3)]
                spin_steps += 1
            else:
                result = [weighted_choice(probabilities) for _ in range(3)]
                if result[0] == result[1] == result[2]:
                    win_message = "You Win!"
                    score += 1
                else:
                    win_message = ""
                spinning = False
        clock.tick(30)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
