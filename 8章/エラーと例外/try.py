# -*- coding: Shift-JIS -*-

#例外処理に必要なのが、try節、except節
try:
    x = 2
    print("10 / x =", 10 / x) #try節
    print("try節終了")
except TypeError:
    print("TypeErrorです") #except節

print("プログラムの終了")