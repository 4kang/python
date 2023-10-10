import this

print("-------文字列-------")
print("HelloWorld")
print("こんにちわ～～眠いですがぼちぼちやってますコノヤロー")
print("Hello", "world")
print("Hello" + "World")
print("I" + "am", "Python")

print("--------分割メソッド--------")
print("Hello Wolrd".split(" "))
print("Hello World".split("e")) #eが消える
print("Hello Wolrd".split())
print("Java Script".split())
print("ABCDEFGHI".split("F"))

print("---------置換メソッド--------")
print("Hello World".replace("o", "A"))
print("Hello World".replace("l", "L"))

print("----------全て大文字に変換するメソッド--------")
print("Hello World".upper())
print("Free to use or reprint fan art image.Enjoy!\nBut please don’t forget to credit.\nNot for commercial use.\nUse for hateful purposes is prohibited.".upper())

print("-------全て小文字にする--------")
print("Hello World".lower())
print("Free to use or reprint fan art image.Enjoy!".lower())

#メソッドの組み合わせ
print("-------大文字に変換して分割-------")
print("Hello World. I am Tack.".upper().split(" "))
print("Hello World. I am Tack. Nice to meet you, Chop! Let's go swimming. Ha, ha, ha, is's a joke!!".upper().split(" "))

#変数
print("-------変数--------")
x = "Hello World"
print(x.upper())

abcd = "無敵の笑顔で沸かすメディア、知ってその秘密ミステリアス、抜けてるとこさえ彼女のエリア、完璧で嘘つきな君は、天才的なアイドル様"
print(abcd)

x = "Good morning"
print(x.upper())

abcd = "Itterasshai"
print(abcd.replace("r", "R"))


print("----------変数に変数をいれる----------")
#変数＝変数
x = "Good morning"
x.upper()
print(x)
#↑だとメソッドが機能されないので・・・
x = x.upper()
print(x)

x = "Hello World"
y = x.upper()
print(y)


#join() ばらされた文字列をつなげる(split必須)
x = "Hello World".split(" ")
print(x)
y = " ".join(x)
print(y)

x = "Hello World".split(" ")
print(x)
y = "my".join(x)
print(y) #HelloとWorldの間にmyが入る


#find() 特定の文字列の順番を数える
x = "Hello World".find("e")
print(x)

print("Hello World".find("W"))
print("Hello World".find("a")) #文字列中にない言葉を検索すると-1と返す


#count() 特定の文字列の数を数える
print("Mississippi".count("s"))
print("Mississippi".count("ss"))
print("Mississippi".count("si"))

#インデックス
print("Hello Wolrd"[1])
x = "Hello World"[-1]
print(x)

#スライシング
x = "Hello World"[1:4]
print(x)

print("対話型コマンドライン↓")
print("Hello World")

#数値というデータ型
#データ型を確認する方法(type)
print(type("Hello World"))
print(type(4))
print(type(1.06))
x = 99
print(type(x))
print("------------数値型で遊んでみる------------")
print(2 + 3 - 1)
print(2 * 8)
