# -*- coding: Shift-JIS -*-


#x = 10 / 0
#ZeroDivisionError: division by zZeroDivisionErroro, eee

# except[��O�̎��]as[�ϐ���]:
try:
    x = 10 / 0
except ZeroDivisionError as eee:
    print(type(eee))
    print(eee.args) #��O�̐�����v�f�Ɏ��^�v��
    print(eee.args[0])
    print(eee)

print("--------------------------------------------")
#[ZeroDivisionError: division by zero]���o��
try:
    x = 10 / 0
except ZeroDivisionError as eee:
    print("ZeroDivisionError", eee)
    
print("--------------------------------------------")
try:
    x = 10 / 0
    #�S�Ă̗�O�ɑ΂���except�߂̃R�[�h�����s������
except Exception as eee:
    print("ZeroDivisionError", eee)