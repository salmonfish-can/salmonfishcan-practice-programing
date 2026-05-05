import tkinter as tk
import pyautogui
import time
root = tk.Tk()
root.title('オートクリッカー')
root.geometry('500x450')
pause = 0
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
def click():
    time.sleep(3)
    i = 0
    count = int(clickinput.get())
    while(i < count):
        pyautogui.click()
        i = i + 1
def updatepause():
    global pause
    temp = pauseinput.get()
    try:
        pause = float(temp)
        pyautogui.PAUSE = pause
    except:
        caution.pack()
caution = tk.Label(root,text="正しく実行できませんでした！")
clickbutton = tk.Button(root, text="クリック開始！",command=click)
clickbutton.pack(pady = 40)
expl = tk.Label(root,text="クリックする回数を入力")
expl.pack(pady = 0)
clickinput = tk.Entry(root, width=10)
clickinput.pack(pady=10)
pausecontrol = tk.Button(root,text="間隔を決定",command=updatepause)
pausecontrol.pack(pady=50)
expl2 = tk.Label(root,text="入力する間隔を入力（デフォルト0）")
expl2.pack(pady = 0)
pauseinput = tk.Entry(root,width=10)
pauseinput.pack(pady=10)
root.mainloop()