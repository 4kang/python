# -*- coding: Shift-JIS -*-
class chara_data:
    def __init__(self):
        self.name = ""
        self.size = 0
        self.seibetu = ""
        self.hair = ""
        self.eyesize = 0
        self.headmoney = 0
        self.bodymoney = 0
        self.heikin = 0

    def heikin_money(self):
        self.heikin = (self.headmoney + self.bodymoney) // 2

imouto = chara_data()
imouto.name = "�~�l�����@"
imouto.size = 40
imouto.seibetu = "���̎q"
imouto.hair = "����"
imouto.eyesize = 22
imouto.headmoney = 40000
imouto.bodymoney = 30000
imouto.heikin_money()

ani = chara_data()
ani.name = "�N���m�A"
ani.size = 60
ani.seibetu = "�j�̎q"
ani.hair = "����"
ani.eyesize = 22
ani.headmoney = 35000
ani.bodymoney = 30000
ani.heikin_money()

print(imouto.name,imouto.size,"cm",imouto.seibetu,imouto.heikin)
print(ani.name,ani.size,"cm",ani.seibetu,ani.heikin)
