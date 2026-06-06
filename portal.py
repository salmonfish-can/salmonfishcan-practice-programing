import tkinter as tk
import time
import json
def initialset():
    setname = username.get()
    if not setname:
        caution.config(text="名前が設定されていません！") 
        return
    setbm = userbirthmonth.get()
    setbd = userbirthday.get()
    if not isinstance(setbd,int) and isinstance(setbm,int):
        if setbd and setbm:
            caution.config(text="誕生日は数字のみ使用できます！")
            return
    if setbm or setbd:
        if not (setbm and setbd):
            caution.config(text="誕生日を入力する場合はどちらも入力してください！")
            return
    startdata = {
        "name": setname,
        "bm": setbd,
        "bd": setbm
    }
    with open("pyportal-usersetting.json","w",encoding="utf-8")as w:
        json.dump(startdata,w,ensure_ascii=False,indent=4)
def showhome(data):
    name = data["name"]
    bm = data['bm']
    bd = data['bd']
    welmessage.config(text=f"ポータルへようこそ、{name}さん。")
root = tk.Tk()
root.title("ホーム")
root.geometry("500x400")
caution = tk.Label(root,text="")
caution.pack(pady=5)
initial = tk.Frame(root)
home = tk.Frame(root)
welcome = tk.Frame(home)
welmessage = tk.Label(welcome,text="")
welmessage.pack(pady=5)
st = tk.Frame(home)
userexpl = tk.Label(initial,text="ユーザー名(必須)")
username = tk.Entry(initial,width=10)
bmexpl = tk.Label(initial,text="生まれた月")
userbirthmonth = tk.Entry(initial,width=10)
bdexpl = tk.Label(initial,text="生まれた日")
userbirthday = tk.Entry(initial,width=10)
setexecute = tk.Button(initial,text="確定",command=initialset)
try:
    with open("pyportal-usersetting.json","r",encoding="utf-8")as r:
        data = json.load(r)
    home.pack()
    welcome.pack()
    showhome(data)
except:
    for c in initial.winfo_children():
        c.pack(pady=5)
    initial.pack()
home.mainloop()