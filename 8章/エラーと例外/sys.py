# -*- coding: Shift-JIS -*-

'''標準ライブラリーのsysモジュールのsys.exc_info()関数を
用いることで、以下のことができる'''

import sys
try:
    x = 10 / 0
except ZeroDivisionError :
    print(sys.exc_info())
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])

print("--------------------------------------------")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError:", sys.exc_info()[1])

print("--------------------------------------------")
#except節で例外の種類を指定しない場合でも使用できる
try:
    x = 10 / 0
except:
    print("ZeroDivisionError:", sys.exc_info()[1])
