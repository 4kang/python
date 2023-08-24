# -*- coding: Shift-JIS -*-


#x = 10 / 0
#ZeroDivisionError: division by zZeroDivisionErroro, eee

# except[例外の種類]as[変数名]:
try:
    x = 10 / 0
except ZeroDivisionError as eee:
    print(type(eee))
    print(eee.args) #例外の説明を要素に持つタプル
    print(eee.args[0])
    print(eee)

print("--------------------------------------------")
#[ZeroDivisionError: division by zero]を出力
try:
    x = 10 / 0
except ZeroDivisionError as eee:
    print("ZeroDivisionError", eee)
    
print("--------------------------------------------")
try:
    x = 10 / 0
    #全ての例外に対してexcept節のコードを実行させる
except Exception as eee:
    print("ZeroDivisionError", eee)