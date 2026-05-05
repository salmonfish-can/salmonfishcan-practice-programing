import tkinter as tk
import pyautogui
import time
root = tk.Tk()
root.title('メモ作成・保存')
root.geometry('500x450')
pause = 0
pyautogui.FAILSAFE = False
pyautogui.PAUSE = pause
def click():
    time.sleep(3)
    i = 0
    count = int(clickinput.get())
    while(i < count):
        pyautogui.click()
        i = i + 1
clickbutton = tk.Button(root, text="クリック開始！",command=click)
clickbutton.pack(pady = 40)
expl = tk.Label(root,text="クリックする回数を入力")
expl.pack(pady = 0)
clickinput = tk.Entry(root, width=10)
clickinput.pack(pady=10)
root.mainloop()