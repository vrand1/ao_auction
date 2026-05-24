import time
from pynput import mouse

print("Скрипт запущен. Кликайте в нужные места на экране.")
print("Для выхода из программы нажмите Ctrl+C в терминале.\n")

def on_click(x, y, button, pressed):
    if pressed:
        # Выводит координаты в удобном формате для копирования
        print(f"({int(x)}, {int(y)}),")

# Слушаем клики мыши
with mouse.Listener(on_click=on_click) as listener:
    listener.join()