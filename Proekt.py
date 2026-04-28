import pygame
import random
import string

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zamok Bot")

# Цветовая палитра (Premium Grey Design)
COLOR_BG = (28, 30, 33)  # Глубокий графит
COLOR_PANEL = (43, 45, 49)  # Матовый серый
COLOR_ACCENT = (200, 200, 200)  # Светлое серебро
COLOR_TEXT_DIM = (120, 125, 130)  # Приглушенный серый
COLOR_GLOW = (255, 255, 255, 30)  # Белый для бликов

# Шрифты
font_main = pygame.font.SysFont("Verdana", 18, bold=True)
font_pass = pygame.font.SysFont("Consolas", 26, bold=True)


def draw_lock_icon(surface, x, y):
    """Стильный стальной замок."""
    # Дужка (серебристая)
    pygame.draw.circle(surface, COLOR_ACCENT, (x, y - 5), 18, width=4, draw_top_left=True, draw_top_right=True)
    # Тело замка (градиентный эффект через два прямоугольника)
    body_rect = pygame.Rect(x - 22, y, 44, 35)
    pygame.draw.rect(surface, COLOR_ACCENT, body_rect, border_radius=4)
    # Деталь (скважина)
    pygame.draw.rect(surface, COLOR_BG, (x - 3, y + 10, 6, 12), border_radius=2)


def generate_premium_password(length=20):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    return ''.join(random.choice(chars) for _ in range(length))


def draw_button(surface, rect, text, is_hovered):
    # Цвет меняется от темно-серого к светло-серому
    base_color = (60, 63, 68) if is_hovered else COLOR_PANEL
    pygame.draw.rect(surface, base_color, rect, border_radius=8)
    # Тонкая серебряная рамка
    pygame.draw.rect(surface, COLOR_ACCENT, rect, width=1, border_radius=8)

    text_surf = font_main.render(text, True, COLOR_ACCENT)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)


def main():
    running = True
    current_password = "• " * 10
    button_rect = pygame.Rect(WIDTH // 2 - 110, 360, 220, 50)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = button_rect.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_hovered:
                    current_password = generate_premium_password(20)

        # Фон
        screen.fill(COLOR_BG)

        # Рисуем замок
        draw_lock_icon(screen, WIDTH // 2, 85)

        # Заголовок
        title_surf = font_main.render("Zamok", True, COLOR_ACCENT)
        screen.blit(title_surf, (WIDTH // 2 - title_surf.get_width() // 2, 140))

        sub_title = font_main.render("256-BIT ENCRYPTION STANDARD", True, COLOR_TEXT_DIM)
        screen.blit(sub_title, (WIDTH // 2 - sub_title.get_width() // 2, 170))

        # Центральная панель для пароля
        pass_box = pygame.Rect(40, 220, 520, 90)
        # Эффект объема
        pygame.draw.rect(screen, (35, 37, 40), pass_box, border_radius=10)
        pygame.draw.rect(screen, (55, 58, 62), pass_box, width=2, border_radius=10)

        pass_surf = font_pass.render(current_password, True, (255, 255, 255))
        pass_text_rect = pass_surf.get_rect(center=pass_box.center)
        screen.blit(pass_surf, pass_text_rect)

        # Кнопка
        draw_button(screen, button_rect, "GENERATE", is_hovered)

        # Подпись внизу
        footer_surf = font_main.render("PREMIUM VERSION v1.0", True, (60, 60, 60))
        screen.blit(footer_surf, (WIDTH // 2 - footer_surf.get_width() // 2, 460))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
