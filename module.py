# -*- coding: utf-8 -*-
import fibo # fibo ���W���[����import�����

# fibo ���W���[���� fib() �֐����Ăяo��
print(fibo.fib(1000))
print(fibo.fib2(100))

# ���W���[���� 'fibo' ���o��
print(fibo.__name__) 

# fibo ���W���[���� fib() �֐������[�J���ϐ��ɑ��
fib = fibo.fib 
print(fib(500))

# fibo ���W���[���� fib(), fib2() �֐�������import
from fibo import fib, fib2
print(fib(300))

# �A���_�[�X�R�A _ �Ŏn�܂�ȊO�̖��O��import
from fibo import *
print(fib(500))

#python fibo.py <arguments>

'''if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))'''

