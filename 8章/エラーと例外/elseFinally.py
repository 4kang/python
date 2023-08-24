# -*- coding: Shift-JIS -*-

print("-------コード05--------")
#try節で例外が生じなかった場合
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

print("-------コード06--------")
#try節で例外発生→except節で指定すると例外と一致
try:
    #TypeErrorの発生
    x = "2"
    print("10 / x =", 10 / x)
    print("Try節終了")
except TypeError:
    #実行
    print("TypeErrorです")
else:
    #try節で例外発生したのでelse節は実行せず
    print("else節の実行")
finally:
    #必ず実行される
    print("finally節の実行")

print("プログラムの終了")

print("-------コード07--------")
try:
    x = 0
    print("10 / x =", 10 / x)
    print("Try節終了")
#例外の種類の不一致→実行せず
except TypeError:
    print("TypeErrorです")
else:
    #これも実行せず
    print("else節の実行")
finally:
    #必ず実行される
    print("finally節の終了")

#　例外を送出。実行を停止
print("プログラムの終了")