# -*- coding: Shift-JIS -*-

'''�W�����C�u�����[��sys���W���[����sys.exc_info()�֐���
�p���邱�ƂŁA�ȉ��̂��Ƃ��ł���'''

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
#except�߂ŗ�O�̎�ނ��w�肵�Ȃ��ꍇ�ł��g�p�ł���
try:
    x = 10 / 0
except:
    print("ZeroDivisionError:", sys.exc_info()[1])
