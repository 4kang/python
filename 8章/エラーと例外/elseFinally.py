# -*- coding: Shift-JIS -*-

try:
    x = 2
    print("10 / x =", 10 / x)
    print("Try節終了")
except TypeError:
    print("TypeErroeです")
else:
    #try節で例外なしなのでelse節は実行
    print("else節の実行") 
finally:
    #必ず実行
    print("finally節の実行")

print("プログラムの終了")