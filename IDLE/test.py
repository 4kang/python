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
