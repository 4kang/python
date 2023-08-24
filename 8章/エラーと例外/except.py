print("-------コード02--------")
#try節の例外が発生してexcept節で指定すると例外と一致

try:
    x = "2"
    #TyptErrorが発生
    print("10 / x =", 10 / x)
    print("try節終了")
#例外タイプが一致→実行
except TypeError: 
    print("TypeErrorです")
    
print("プログラムの終了")

print("-------コード03--------")

# except節で指定する例外と一致しない
try:
    x = 0
    print("10 / x =", 10 / x)
    print("Try節終了")
#例外の種類の不一致→実行せず
except TypeError:
    print("TypeErrorです")
#　例外を送出。実行を停止
print("プログラムの終了")