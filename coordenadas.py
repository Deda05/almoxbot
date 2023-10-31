import pyautogui as pt
import time

while True:
    time.sleep(5)
    x, y = pt.position()
    print(x,y)
    break

