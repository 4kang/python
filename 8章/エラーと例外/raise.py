# -*- coding: Shift-JIS -*-

#��O���Ӑ}�I�ɔ���������

try:
    raise ZeroDivisionError
except ZeroDivisionError as eee:
    print("eee.args:", eee.args)
    print("eee", eee)


print("\nraise�Ŕ������������u��O�̎�ށv�̌��()�̂Ȃ��Ɂu��O�̏��v�𕶎���^�ŋL��")

try:
    raise ZeroDivisionError("�[���ɂ�鏜�Z")
except ZeroDivisionError as eee:
    print("eee.args", eee.args)
    print("eee", eee)

print("\n�܂�2�ȏ�́u��O�̏��v���L�����邱�Ƃ��ł���")

import sys

try:
    raise ZeroDivisionError("�[���ɂ�鏜�Z","2�ڂ̏��")
except ZeroDivisionError as eee:
    print("eee", eee)
    print("eee.args", eee.args) #��O�̐�����v�f�Ɏ��^�v��
    print("eee.args[0]", eee.args[0]) #[0]�̓C���f���g
    print("eee.args[1]", eee.args[1]) 