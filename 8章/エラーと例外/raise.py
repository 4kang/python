# -*- coding: Shift-JIS -*-

#例外を意図的に発生させる

try:
    raise ZeroDivisionError
except ZeroDivisionError as eee:
    print("eee.args:", eee.args)
    print("eee", eee)


print("\nraiseで発生させたい「例外の種類」の後の()のなかに「例外の情報」を文字列型で記入")

try:
    raise ZeroDivisionError("ゼロによる除算")
except ZeroDivisionError as eee:
    print("eee.args", eee.args)
    print("eee", eee)

print("\nまた2つ以上の「例外の情報」を記入することができる")

import sys

try:
    raise ZeroDivisionError("ゼロによる除算","2つ目の情報")
except ZeroDivisionError as eee:
    print("eee", eee)
    print("eee.args", eee.args) #例外の説明を要素に持つタプル
    print("eee.args[0]", eee.args[0]) #[0]はインデント
    print("eee.args[1]", eee.args[1]) 