import tkinter as tk
import pyautogui
import time
root = tk.Tk()
root.title('オートクリッカー')
root.geometry('500x450')
pause = 0
failsafe = True
mode = 0
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
        return
    while(i < count):
        pyautogui.click()
        i = i + 1
def easyclick(count):
    time.sleep(3)
    i = 0
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
        return
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
def modechange():
    global mode
    if(mode == 0):
        mode = 1
        normal.pack_forget()
        easy.pack()
    else:
        mode = 0
        easy.pack_forget()
        normal.pack()
normal = tk.Frame(root,pady=10)
easy = tk.Frame(root,pady=10)
caution = tk.Label(normal,text="正しく実行できませんでした！")
clickbutton = tk.Button(normal, text="クリック開始！",command=click)
clickbutton.pack(pady = 40)
expl = tk.Label(normal,text="クリックする回数を入力")
expl.pack(pady = 0)
clickinput = tk.Entry(normal, width=10)
clickinput.pack(pady=10)
pausecontrol = tk.Button(normal,text="間隔を決定",command=updatepause)
pausecontrol.pack(pady=50)
expl2 = tk.Label(normal,text="入力する間隔を入力（デフォルト0）")
expl2.pack(pady = 0)
pauseinput = tk.Entry(normal,width=10)
pauseinput.pack(pady=10)
failsafebutton = tk.Button(normal,text="failsafeを切り替え（デフォルトはON）",command=failsafeonoff)
failsafebutton.pack(pady=10)
failsafeon = tk.Label(normal,text="現在failsafeはONです")
failsafeoff = tk.Label(normal,text="現在failsafeはOFFです")
failsafeon.pack(pady=10)
modebutton = tk.Button(root,text="モード切り替え",command=modechange)
click100 = tk.Button(easy,text="100回クリック",command=lambda: easyclick(100))
click100.pack()
click1000 = tk.Button(easy,text="1000回クリック",command=lambda: easyclick(1000))
click1000.pack()
modebutton.pack()
normal.pack()
easy.pack_forget()
root.mainloop()