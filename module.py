# -*- coding: utf-8 -*-
import fibo # fibo モジュールがimportされる

# fibo モジュールの fib() 関数を呼び出す
print(fibo.fib(1000))
print(fibo.fib2(100))

# モジュール名 'fibo' を出力
print(fibo.__name__) 

# fibo モジュールの fib() 関数をローカル変数に代入
fib = fibo.fib 
print(fib(500))

# fibo モジュールの fib(), fib2() 関数だけをimport
from fibo import fib, fib2
print(fib(300))

# アンダースコア _ で始まる以外の名前をimport
from fibo import *
print(fib(500))

#python fibo.py <arguments>

'''if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))'''

