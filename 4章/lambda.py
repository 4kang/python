# -*- coding: utf-8 -*-
dive_code = [(1, "Sora"),(2, "Hotaru"),(3,"Yoshiki"),(4,"Tanko")]

# dicにdive_codeリストを代入
dic = dive_code 
# 1は第二要素の名前を昇順にする。0の場合、第一要素の数字に対し昇順にする。
dic.sort(key=lambda dic: dic[1])

print(dic)

# 2回目
code_args = [(2, "Hotaru"),(4, "Tanko"),(1, "Sora"),(3, "Yoshiki")]
dic2 = code_args

# 0の場合、第一要素の数字に対し昇順にする。
dic2.sort(key=lambda dic2: dic2[0])
print(dic2)

dive_code2 = [(1, "Uni"),(2, "Arisu"),(3, "Kaori"),(4, "Jin"),(5, "Hoshi")]

dic3 = dive_code2
dic3.sort(key=lambda dic3: dic3[1])

print(dic3)

dictionary = [["nara",3], ["kanagawa",4], ["tokyo",1], ["osaka", 2]]
print(dictionary)

sortedDict = sorted(dictionary, key=lambda x: x[1])
print(sortedDict)