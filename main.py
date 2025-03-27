import keyboard

import time

from pynput.mouse import Button, Controller, Listener
# Создаем объект контроллера мыши
mouse1 = Controller()

def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        print(f"Mouse clicked at ({x}, {y}) with Button.left")

def perform_macro():
    coordinates = [(842, 652), (840, 614), (888, 782), (814, 606)]
    #842, 584   842, 652 814, 606
    mouse1.position = coordinates[0]
    mouse1.click(Button.left)
    time.sleep(0.2)
    mouse1.position = coordinates[1]
    for i in range(1):
        mouse1.click(Button.left)
        time.sleep(0.1)
    time.sleep(0.2)
    mouse1.position = coordinates[2]
    mouse1.click(Button.left)
    time.sleep(0.2)
    mouse1.position = coordinates[3]
    mouse1.click(Button.left)
    time.sleep(0.2)
    mouse1.position = (1328, 400)
    time.sleep(0.4)  # Задержка для реалистичности



def perform_macro2():
    coordinates = [(1350, 406), (462, 510), (468,662), (860, 784)]

    time.sleep(0.2)
    mouse1.position = coordinates[0]
    mouse1.click(Button.left)
    time.sleep(0.2)
    mouse1.position = coordinates[1]
    mouse1.click(Button.left)
    time.sleep(0.2)
    mouse1.position = coordinates[2]
    mouse1.click(Button.left)
    time.sleep(0.2)
    mouse1.position = coordinates[3]
    mouse1.click(Button.left)

keyboard.add_hotkey('F1', perform_macro) # выставление заказа
keyboard.add_hotkey('F3', perform_macro2) # продажа первого предмета

print("Макрос назначен на клавишу F1. Нажмите F1 для выполнения макроса.")
with Listener(on_click=on_click) as listener:
    listener.join()
# Бесконечный цикл для поддержания работы скрипта
keyboard.wait('esc')  # Выход из скрипта при нажатии клавиши 'esc'

