print("-------�R�[�h02--------")
#try�߂̗�O����������except�߂Ŏw�肷��Ɨ�O�ƈ�v

try:
    x = "2"
    #TyptError������
    print("10 / x =", 10 / x)
    print("try�ߏI��")
#��O�^�C�v����v�����s
except TypeError: 
    print("TypeError�ł�")
    
print("�v���O�����̏I��")

print("-------�R�[�h03--------")

# except�߂Ŏw�肷���O�ƈ�v���Ȃ�
try:
    x = 0
    print("10 / x =", 10 / x)
    print("Try�ߏI��")
#��O�̎�ނ̕s��v�����s����
except TypeError:
    print("TypeError�ł�")
#�@��O�𑗏o�B���s���~
print("�v���O�����̏I��")