# -*- coding: Shift-JIS -*-

try:
    x = 2
    print("10 / x =", 10 / x)
    print("Try�ߏI��")
except TypeError:
    print("TypeErroe�ł�")
else:
    #try�߂ŗ�O�Ȃ��Ȃ̂�else�߂͎��s
    print("else�߂̎��s") 
finally:
    #�K�����s
    print("finally�߂̎��s")

print("�v���O�����̏I��")