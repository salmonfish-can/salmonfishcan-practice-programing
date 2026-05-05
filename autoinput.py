import tkinter as tk
import pyperclip
import pyautogui
import time
root = tk.Tk()
root.title('自動入力用')
root.geometry('500x900')
pause = 0.1
failsafe = True
mode = 0
enter = 0
pyautogui.FAILSAFE = failsafe
pyautogui.PAUSE = 0.1
def click():
    i = 0
    try:
        count = int(clickinput.get())
        caution.pack_forget()
        if not(count >= 0):
            caution.pack()
            return
    except:
        caution.pack()
        return
    time.sleep(3)
    while(i < count):
        pyautogui.click()
        i = i + 1
def easyclick(count):
    time.sleep(3)
    i = 0
    while(i < count):
        pyautogui.click()
        i = i + 1
def character():
    global enter
    i = 0
    try:
        content = str(characterinput.get("1.0", "end-1c"))
        count = int(charactercount.get())
        if not(count >= 0):
            caution.pack()
            return
    except:
        caution.pack()
        return
    time.sleep(3)
    pyperclip.copy(content)
    if(enter == 0):
        while(i < count):
            pyautogui.hotkey("ctrl","v")
            i = i + 1
    else:
        while(i < count):
            pyautogui.hotkey("ctrl","v")
            pyautogui.press("enter")
            i = i + 1
def enterchange():
    global enter
    if(enter == 0):
        enter = 1
        enterlabel.config(text="エンターキー:押す")
    else:
        enter = 0
        enterlabel.config(text="エンターキー:押さない")
def updatepause():
    global pause
    temp = pauseinput.get()
    try:
        pause = float(temp)
        if not(pause >= 0):
            caution.pack()
            return
        pyautogui.PAUSE = pause
        caution.pack_forget()
        disptemp = str(temp)
        nowpause.config(text="間隔:" + disptemp + "秒ごとに一回")
    except:
        caution.pack()
        return
def easyupdatepause(newpause):
    global pause
    pause = newpause
    pyautogui.PAUSE = pause
    dispnewpause = str(newpause)
    nowpause.config(text="間隔:" + dispnewpause + "秒ごとに一回")
def failsafeonoff():
    global failsafe
    if(failsafe == True):
        failsafe = False
        pyautogui.FAILSAFE = failsafe
        failsafelabel.config(text="現在failsafeはOFFです")
    else:
        failsafe = True
        pyautogui.FAILSAFE = failsafe
        failsafelabel.config(text="現在failsafeはONです")
def modechange():
    global mode
    if(mode == 0):
        mode = 1
        normal.pack_forget()
        easypause.pack_forget()
        easy.pack()
        easypause.pack()
    else:
        mode = 0
        easy.pack_forget()
        easypause.pack_forget()
        normal.pack()
        easypause.pack()
normal = tk.Frame(root,pady=10)
easy = tk.Frame(root,pady=10)
easypause = tk.Frame(root,pady=10)
caution = tk.Label(normal,text="正しく実行できませんでした！")
clickbutton = tk.Button(normal, text="クリック開始！",command=click)
clickbutton.pack(pady = 40)
expl = tk.Label(normal,text="クリックする回数を入力")
expl.pack(pady = 0)
clickinput = tk.Entry(normal, width=10)
clickinput.pack(pady=10)
pausecontrol = tk.Button(normal,text="間隔を決定",command=updatepause)
pausecontrol.pack(pady=50)
expl2 = tk.Label(normal,text="入力する間隔を入力（デフォルト0.1）")
expl2.pack(pady = 0)
pauseinput = tk.Entry(normal,width=10)
pauseinput.pack(pady=10)
nowpause = tk.Label(normal,text="間隔:0.1秒ごとに一回")
nowpause.pack()
failsafebutton = tk.Button(normal,text="failsafeを切り替え",command=failsafeonoff)
failsafebutton.pack(pady=10)
failsafelabel = tk.Label(normal,text="現在failsafeはONです")
failsafelabel.pack(pady=10)
characterlabel = tk.Label(normal,text="文字を入力")
characterlabel.pack(pady=0)
characterinput = tk.Text(normal,width=20,height=3)
characterinput.pack(pady=0)
characterlabel2 = tk.Label(normal,text="回数を入力")
characterlabel2.pack(pady=0)
charactercount = tk.Entry(normal,width=10)
charactercount.pack(padx=0,pady=0)
characterbutton = tk.Button(normal,text="出力",command=character)
characterbutton.pack(pady=10)
enterlabel = tk.Label(normal,text="エンターキー:押さない")
enterlabel.pack(pady=0)
enterbutton = tk.Button(normal,text="１回毎にエンターキーを押すかを切り替え",command=enterchange)
enterbutton.pack(pady=10)
pause00 = tk.Button(easypause,text="0秒間隔",command=lambda: easyupdatepause(0))
pause01 = tk.Button(easypause,text="0.1秒間隔",command=lambda: easyupdatepause(0.1))
pause03 = tk.Button(easypause,text="0.3秒間隔",command=lambda: easyupdatepause(0.3))
pause05 = tk.Button(easypause,text="0.5秒間隔",command=lambda: easyupdatepause(0.5))
pause00.pack()
pause01.pack()
pause03.pack()
pause05.pack()
modebutton = tk.Button(root,text="モード切り替え",command=modechange)
click100 = tk.Button(easy,text="100回クリック",command=lambda: easyclick(100))
click100.pack()
click1000 = tk.Button(easy,text="1000回クリック",command=lambda: easyclick(1000))
click1000.pack()
click10000 = tk.Button(easy,text="10000回クリック",command=lambda: easyclick(10000))
click10000.pack()
modebutton.pack()
normal.pack()
easypause.pack()
easy.pack_forget()
root.mainloop()