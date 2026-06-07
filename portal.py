import tkinter as tk
from tkinter import messagebox
import time
import json
import os
def initialset():
    setname = username.get()
    if not setname:
        caution.config(text="名前が設定されていません！") 
        return
    setbm = userbirthmonth.get()
    setbd = userbirthday.get()
    try:
        int(setbm)
        int(setbd)
    except:
        caution.config(text="誕生日は数字のみ使用できます！")
        return
    if setbm or setbd:
        if not (setbm and setbd):
            caution.config(text="誕生日を入力する場合はどちらも入力してください！")
            return
    startdata = {
        "name": setname,
        "bm": setbm,
        "bd": setbd
    }
    startmemo = []
    with open("pyportal-usersetting.json","w",encoding="utf-8")as w:
        json.dump(startdata,w,ensure_ascii=False,indent=4)
    with open("pyportal-memo.json","w",encoding="utf-8")as w:
        json.dump(startmemo,w,ensure_ascii=False,indent=4)
def showhome():
    try:
        with open("pyportal-usersetting.json","r",encoding="utf-8")as r:
            data = json.load(r)
            name = data["name"]
            bm = data['bm']
            bd = data['bd']
            home.pack()
            welcome.pack()
            welmessage.config(text=f"ポータルへようこそ、{name}さん。")
            st.pack()
            
    except:
        for c in initial.winfo_children():
            c.pack(pady=5)
    initial.pack()
def creatememo():
    memoname = memoinput.get()
    memotext = memonaiyou.get("1.0","end-1c")
    if(os.path.exists(f"{memoname}.json")):
        caution.config(text="その名前のメモはすでに存在します！編集する場合は開いて編集ボタンを押してください！")
        return
    memodata = {
        "title": memoname,
        "text": memotext
    }
    memotd = {
        "title": memoname
    }
    with open(f"{memoname}.json","w",encoding="utf-8")as w:
        json.dump(memodata,w,ensure_ascii=False,indent=4)
    with open("pyportal-memo.json","r",encoding="utf-8")as r:
        data = json.load(r)
        data.append(memotd)
    with open(f"pyportal-memo.json","w",encoding="utf-8")as w:
        json.dump(data,w,ensure_ascii=False,indent=4)
    create.pack_forget()
    home.pack()
    caution.config(text="メモの作成が完了しました！")
def memoscreen():
    home.pack_forget()
    create.pack()
def showmemo():
    memoname = memoreadinput.get()
    if(memoname == ""):
        with open(f"pyportal-memo.json","r",encoding="utf-8")as r:
            memotitle.config(text="[メモ一覧]")
            data = json.load(r)
            t = []
            for d in data:
                t.append(f"・{d['title']}")
            memolist = '\n'.join(t)
            memotext.config(text=memolist)
            home.pack_forget()
            memoread.pack()
            return
    try:
        with open(f"{memoname}.json","r",encoding="utf-8")as r:
            data = json.load(r)
            title = data['title']
            text = data['text']
            memotitle.config(text=title)
            memotext.config(text=text)
            home.pack_forget()
            memoread.pack()
    except:
        caution.config(text="そのようなタイトルのメモは存在しません！")
def memobackhome():
    home.pack()
    memoread.pack_forget()
root = tk.Tk()
root.title("ホーム")
root.geometry("500x400")
caution = tk.Label(root,text="")
caution.pack(pady=5)
home = tk.Frame(root)
welcome = tk.Frame(home)
welmessage = tk.Label(welcome,text="")
welmessage.pack(pady=5)
st = tk.Frame(home)
memocreate = tk.Button(st,text="メモを作成",command=memoscreen)
memocreate.pack(pady=5)
memoshow = tk.Button(st,text="メモを見る",command=showmemo)
memoshow.pack(pady=0,padx=5)
memoreadinput = tk.Entry(st,width=20)
memoreadinput.pack(pady=5)
initial = tk.Frame(root)
userexpl = tk.Label(initial,text="ユーザー名(必須)")
username = tk.Entry(initial,width=10)
bmexpl = tk.Label(initial,text="生まれた月")
userbirthmonth = tk.Entry(initial,width=10)
bdexpl = tk.Label(initial,text="生まれた日")
userbirthday = tk.Entry(initial,width=10)
setexecute = tk.Button(initial,text="確定",command=initialset)
create = tk.Frame(root)
memoinput = tk.Entry(create,width=20)
memoinput.pack(pady=5)
memonaiyou = tk.Text(create,width=40,height=30)
memonaiyou.pack()
memoconfirm = tk.Button(create,text="メモを作成",command=creatememo)
memoconfirm.pack()
memoread = tk.Frame(root)
memotitle = tk.Label(memoread)
memotext = tk.Label(memoread)
memotitle.pack(pady=5)
memotext.pack(pady=5)
memoback = tk.Button(memoread,text="戻る",command=memobackhome)
memoback.pack(pady=5)
showhome()
root.mainloop()