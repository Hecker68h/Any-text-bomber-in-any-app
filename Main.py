import pyautogui
import time

time.sleep(3)
count = 0
while count <= 4:
    pyautogui.typewrite("you can write anything here" + str(count))
    pyautogui.press("enter")
    count = count + 1
