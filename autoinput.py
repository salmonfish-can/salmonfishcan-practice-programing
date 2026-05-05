import tkinter as tk
import pyautogui
import time
root = tk.Tk()
root.title('オートクリッカー')
root.geometry('500x450')
pause = 0
failsafe = True
pyautogui.FAILSAFE = failsafe
pyautogui.PAUSE = 0
def click():
    time.sleep(3)
    i = 0
    try:
        count = int(clickinput.get())
        caution.pack_forget()
    except:
        caution.pack()
    while(i < count):
        pyautogui.click()
        i = i + 1
def updatepause():
    global pause
    temp = pauseinput.get()
    try:
        pause = float(temp)
        pyautogui.PAUSE = pause
        caution.pack_forget()
    except:
        caution.pack()
def failsafeonoff():
    global failsafe
    if(failsafe == True):
        failsafe = False
        pyautogui.FAILSAFE = failsafe
        failsafeon.pack_forget()
        failsafeoff.pack(pady=10)
    else:
        failsafe = True
        pyautogui.FAILSAFE = failsafe
        failsafeoff.pack_forget()
        failsafeon.pack(pady=10)
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
failsafebutton = tk.Button(root,text="failsafeを切り替え（デフォルトはON）",command=failsafeonoff)
failsafebutton.pack(pady=10)
failsafeon = tk.Label(root,text="現在failsafeはONです")
failsafeoff = tk.Label(root,text="現在failsafeはOFFです")
failsafeon.pack(pady=10)
root.mainloop()