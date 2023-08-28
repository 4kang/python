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
imouto.name = "ミネルヴァ"
imouto.size = 40
imouto.seibetu = "女の子"
imouto.hair = "黒髪"
imouto.eyesize = 22
imouto.headmoney = 40000
imouto.bodymoney = 30000
imouto.heikin_money()

ani = chara_data()
ani.name = "クロノア"
ani.size = 60
ani.seibetu = "男の子"
ani.hair = "黒髪"
ani.eyesize = 22
ani.headmoney = 35000
ani.bodymoney = 30000
ani.heikin_money()

print(imouto.name,imouto.size,"cm",imouto.seibetu,imouto.heikin)
print(ani.name,ani.size,"cm",ani.seibetu,ani.heikin)
