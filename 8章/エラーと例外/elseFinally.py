# -*- coding: Shift-JIS -*-

print("-------�R�[�h05--------")
#try�߂ŗ�O�������Ȃ������ꍇ
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

print("-------�R�[�h06--------")
#try�߂ŗ�O������except�߂Ŏw�肷��Ɨ�O�ƈ�v
try:
    #TypeError�̔���
    x = "2"
    print("10 / x =", 10 / x)
    print("Try�ߏI��")
except TypeError:
    #���s
    print("TypeError�ł�")
else:
    #try�߂ŗ�O���������̂�else�߂͎��s����
    print("else�߂̎��s")
finally:
    #�K�����s�����
    print("finally�߂̎��s")

print("�v���O�����̏I��")

print("-------�R�[�h07--------")
try:
    x = 0
    print("10 / x =", 10 / x)
    print("Try�ߏI��")
#��O�̎�ނ̕s��v�����s����
except TypeError:
    print("TypeError�ł�")
else:
    #��������s����
    print("else�߂̎��s")
finally:
    #�K�����s�����
    print("finally�߂̏I��")

#�@��O�𑗏o�B���s���~
print("�v���O�����̏I��")