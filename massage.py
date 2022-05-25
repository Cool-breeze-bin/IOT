from time import sleep

import pyautogui

# print(pyautogui.position())
pyautogui.moveTo(1252,613)
sleep(0.2)
pyautogui.click()#当前位置单击
# pyautogui.write('服务卡片',interval=0.2)
for i in range(1000):
    pyautogui.hotkey('command','v')
    sleep(0.2)
    pyautogui.hotkey('enter')
