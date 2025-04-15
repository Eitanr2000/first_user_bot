import pyautogui
import time
import cv2
import numpy as np

# Конфигурация игры
GRID_SIZE = 4  # Размер таблицы 4x4
SQUARE_SIZE = 100  # Размер одного квадрата в пикселях
GRID_TOP_LEFT = (550, 200)  # Координаты верхнего левого угла таблицы
DELAY_BETWEEN_TURNS = 2  # Задержка между ходами

# Функция для определения позиций квадратов в таблице
def get_square_positions(grid_top_left, grid_size, square_size):
    positions = []
    for row in range(grid_size):
        for col in range(grid_size):
            x = grid_top_left[0] + col * square_size
            y = grid_top_left[1] + row * square_size
            positions.append((x + square_size // 2, y + square_size // 2))
    return positions

# Считывание экрана
def capture_screen(region):
    screenshot = pyautogui.screenshot(region=region)
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Определение зелёных квадратов
def detect_green_squares(screen, threshold=(50, 255, 50)):
    hsv_image = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 150, 190])  # Нижняя граница зелёного
    upper_green = np.array([70, 255, 255])  # Верхняя граница зелёного
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    positions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 20 and h > 20:  # Фильтр по размеру
            positions.append((x + w // 2, y + h // 2))
    return positions

# Симуляция кликов
def click_sequence(positions):
    for pos in positions:
        pyautogui.click(pos)
        time.sleep(0.2)  # Небольшая пауза между кликами

# Главный цикл игры
def play_memory_game():
    print("Запуск бота...")
    time.sleep(3)  # Время, чтобы открыть игру
    sequence = []  # Последовательность кликов
    square_positions = get_square_positions(GRID_TOP_LEFT, GRID_SIZE, SQUARE_SIZE)
    region = (GRID_TOP_LEFT[0], GRID_TOP_LEFT[1], GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE)

    while True:
        screen = capture_screen(region)
        green_squares = detect_green_squares(screen)

        # Поиск индексов зелёных квадратов
        for square in green_squares:
            for idx, pos in enumerate(square_positions):
                if abs(square[0] - pos[0]) < SQUARE_SIZE // 2 and abs(square[1] - pos[1]) < SQUARE_SIZE // 2:
                    if idx not in sequence:
                        sequence.append(idx)

        # Симуляция кликов
        click_sequence([square_positions[idx] for idx in sequence])
        time.sleep(DELAY_BETWEEN_TURNS)

if __name__ == "__main__":
    play_memory_game()
