# -*- coding: utf-8 -*-
# keys()
member = {1: "Sora", 2: "Hotaru", 3: "Pimon"}
member[4] = "Tarutariya" #4番目を追加

del member[3] #3番目の辞書を削除
print(list(member.keys()))

print("\n---------------------------------")

# values()
member2 = {1: "Xiao", 2: "Zhonli", 3: "Kanu"}
member2[4] = "Qiqi"
print(list(member2.values()))