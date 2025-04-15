import pyautogui

print("Щёлкните мышью в нужной точке. Нажмите 'Ctrl+C', чтобы завершить.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Координаты: x={x}, y={y}", end="\r")
except KeyboardInterrupt:
    print("\nВыход из программы.")
