import pyperclip
def askcopy():
    yesno = input()
    if(yesno == "y"):
        pyperclip.copy(disp)
    elif(yesno == "n"):
        print("nが入力されたので、コピーを行いませんでした。")
    else:
        print("もう一度入力してください...")
        askcopy()
def htmclean(htmz):
    tags = ['<br>','</br>','<p>','</p>','<script>','</script>']
    for tag in tags:
        htmz = htmz.replace(tag,"")
    return(htmz)
print('元の文字列を入力...(エンターキーをニ回押すと確定されます)')
hojo = []
while True:
    temp = str(input())
    if(temp == ""):
        userinput = "\n".join(hojo)
        break
    hojo.append(temp)
print('除外する文字を入力...($_$+コマンドでコマンドを使えます)')
ex = input()
htm = False
if(ex == "$_$html"):
    htm = True
    ex = ""
tx = userinput.splitlines()
res = []
for t in tx:
    if(htm == True):
        cleaned = htmclean(t)
        res.append(cleaned)
        continue
    if(ex in t):
        cleaned = t.replace(ex, "")
        res.append(cleaned)
    else:
        res.append(t)
disp = "\n".join(res)
print(disp)
print('クリップボードに貼り付けますか?(y/n)')
askcopy()