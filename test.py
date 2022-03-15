"""
基本文法まとめ
"""

#文字出力
print ("hogehoge !!")

#変数定義
msg = "hugahuga !!"
print(msg)

#配列
arr = []
print(arr)
arr = ["hoge", "huga"]
print(arr)
print(arr[1]) #huga

#二次元配列
arr = [["hoge", "huga"], [0, 1, 2]]
print(arr)
print(arr[0][1]) #huga
print(arr[1][2]) #2

#定数
DEV_CONST = "dev_const !!"
print(DEV_CONST)

#キャスト------------------------------------

#str
price  = 1000
result = str(price) + "yen"
print(result)

#int
unit  = "10units"
price = "100yen"
total = "total:" + str(int(unit[:2]) * int(price[:3])) + "yen"
print(total)

#処理中断 ------------------------------------
# quit()

#計算 ------------------------------------
x = 10
#割り算
print(x / 6) #1.6666666666666667

# 除算
print(x // 6) #1

# 余り
print(x % 4) #2

#べき乗
print(3 ** 3) #27

#真偽値 ------------------------------------
# True or false
print(True and False) #False
print(True or False) #True
print(not True) #False
print(not False) #True

#TRUE,true,FALSE,falseはだめみたい


#文字連結、繰り返し ----------------------------

print("hoge"+"huga")
print("nandeyanen-" * 3)


#if文 ------------------------------------

val   = 10
limit = 5
if val > limit:
    print("over")
elif val == limit:
    print("just")
else:
    print("under")

# 条件演算
print("Over !!" if val > limit else "Under !!")

#ループ ----------------------------------------
#while
i = 0
while i < 10:
    if i == 12:
        break
    val = "a" if i == 0 else "ta"
    print("%d:%s"%(i,val))
    i += 1
else:
    print("omaehamou..shindeiru..")

#for
#range(0,8)で0-7の集合体
target = 5
for i in range(0,8):
    if i == target:
        #break
        # iが5の時にスキップする。
        continue
    print(i)
#終了後の処理
else:
    print(str(target) + "以外実行 !!")


#関数 ------------------------------------
#
def sayNyanco(name="zizi",age="6"):
    print("Wow! {0} is {1} old years!!".format(name,age))

# 関数呼び出し
sayNyanco("Tama",12)
sayNyanco("Dora",120)
sayNyanco() #既定値呼び出し

