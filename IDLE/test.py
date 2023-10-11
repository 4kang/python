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
print(2 ** 3)
print(12 // 3)
print(12 // 5)
print(12.0 / 5.0)
print(12.0 / 5)

print("--------------文字列と掛け算--------------")
print("Integer Float String" * 10)
print(5 *(2 + 3))
print(type("39"))
print("I am 39 years old".find("39"))

print("I am 39 years old".find(str(39)))
x = "3"
y = "7"
print(int(x) * int(y))
print(type(str(int(str(39)))))
print("It's", 6, "PM.")
print("It's" + "6" + "PM")
#print("It's" + 6 + "PM") #エラー
print("これは", "数字の", "6", "です")

#文字列フォーマット
print("I am {}.".format("John"))
#変数で使うフォーマット
x = "John"
print("I am {}.".format(x))
#複数の変数代入
x = "John"
y = "Yoko"
print("I am {}. You are {}.".format(x, y))
#変数に数値を代入
x = "John"
y = 58
print("I am {}, {}years old.".format(x, y))
#formatメソッドは自動で番号に割り当てられる
x = "John"
print("I am {0}. {0} is my name.".format(x))

#2つの値を渡す例
x = "John"
y = "Tokyo"
print("This is {0}. {1} is {0}'s hometown.".format(x, y))

x = "蛍"
y = "空"
z = "天理"

print("貴方はどちらの主人公を選びますか。{0}？{1}？{2}は{0}を選んだ。".format(x,y,z))

#もう一つの文字列フォーマット
x = "John"
print("I am %s."%x)

x = "John"
y = "Yoko"
print("I am %s. You are %s."%(x,y))
