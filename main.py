import keyboard

import time

from pynput.mouse import Button, Controller, Listener
mouse1 = Controller()

orderBuyCounter = 2; # количество выставляемых предметов
addBuyCount = (892, 580) # повышение количества
addBuyValue = (886, 608) # повышение цены (по кнопке на +1)
executeOrder = (898, 681) # выставление заказа
confirmExecute = (883, 548) # подтверждение выставления
rotateCursor = (1141, 460) # возврат курсора на вверх

def click_at(coords, delay=0.2):
    mouse1.position = coords
    mouse1.click(Button.left)
    time.sleep(delay)

def click_at_buy_counter(coords, count = 2):
    mouse1.position = coords  
    for i in range(count):
        mouse1.click(Button.left)
        time.sleep(0.1)
    time.sleep(0.1)

def perform_macro():
    click_at(addBuyValue)
  
    click_at_buy_counter(addBuyCount)
  
    click_at(executeOrder)

    click_at(confirmExecute)
  
    mouse1.position = rotateCursor # возврат курсора на вверх



keyboard.add_hotkey('F1', perform_macro) # выставление заказа

print("Макрос назначен на клавишу F1. Нажмите F1 для выполнения макроса.")

keyboard.wait('esc')  
print("Скрипт завершил работу.")

