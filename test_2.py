
#データ入力 -----------------------------------
# str = input("input word：")
# print("result：" + str)


#型 -------------------------------------------
def getTypeString (s):
    print(type(s))
    if type(s) is str:
        print("String")
    elif type(s) is int:
        print("Integer")
    elif type(s) is bool:
        print("Bool")
    else:
        print("Float")

s = "aaa" # str
getTypeString(s)
s = 1 # int
getTypeString(s)
s = 2.5555 # float
getTypeString(s)
s = True # bool
getTypeString(s)

# <class 'str'>
# String
# <class 'int'>
# Integer
# <class 'float'>
# Float
# <class 'bool'>
# Bool


# for -----------------------------------

#一文字ずつ出力
def splitStr (s):
    for i in s:
        print(i)

s = "あいうえお"
splitStr(s)
s = "123"
splitStr(s)

# あ
# い
# う
# え
# お
# 1
# 2
# 3

# 空が入力されるまで要求
# WhileにTrueを渡す事で処理継続実行
# breakの条件合致で処理停止
# while True:
#     s = input("文字入力してください：")
#     print("入力文字：" + s)
#     if s == "":
#         print("処理を停止します。")
#         break

# 扇形の面積
# l(length) = 一辺の長さ 
# a(angle)  = 中心角
def calcFanSharpedArea (l, a, d=""):
    pi = 3.14
    r = 2 * l * pi * (a / 360)
    d = ".2f" if d == "" else "." + str(d) + "f"
    return format(r, d)


l = 6
a = 30
r = calcFanSharpedArea(l, a, 15)
s = "一辺が" + str(l) + "cm、"
s += "中心角が" + str(a) + "°の"
s += "扇形の面積は" + str(r) + "(cm)です。"
print(s)

#乱数 -----------------------------------------------

import random
r = random.randint(1,6);
print(r)
r = random.random();
print(r)

#引数までの値を加算して返す
def addCnt (n):
    r = 0
    for i in range(1, n+1):
        r += i
    return r

print(addCnt(10))

def addCnt2 (n):
    a = (1 + n) * n/2
    return int(a)
print(addCnt2(10))


#九九 ---------------------------------------------

def kuku ():
    for i in range (1, 10):
        k = ""
        for j in range (1, 10):
            k += "{}*{}={:2d}  ".format(i, j,i*j)
        print(k)
kuku()

# 1*1= 1  1*2= 2  1*3= 3  1*4= 4  1*5= 5  1*6= 6  1*7= 7  1*8= 8  1*9= 9
# 2*1= 2  2*2= 4  2*3= 6  2*4= 8  2*5=10  2*6=12  2*7=14  2*8=16  2*9=18
# 3*1= 3  3*2= 6  3*3= 9  3*4=12  3*5=15  3*6=18  3*7=21  3*8=24  3*9=27
# 4*1= 4  4*2= 8  4*3=12  4*4=16  4*5=20  4*6=24  4*7=28  4*8=32  4*9=36
# 5*1= 5  5*2=10  5*3=15  5*4=20  5*5=25  5*6=30  5*7=35  5*8=40  5*9=45
# 6*1= 6  6*2=12  6*3=18  6*4=24  6*5=30  6*6=36  6*7=42  6*8=48  6*9=54
# 7*1= 7  7*2=14  7*3=21  7*4=28  7*5=35  7*6=42  7*7=49  7*8=56  7*9=63
# 8*1= 8  8*2=16  8*3=24  8*4=32  8*5=40  8*6=48  8*7=56  8*8=64  8*9=72
# 9*1= 9  9*2=18  9*3=27  9*4=36  9*5=45  9*6=54  9*7=63  9*8=72  9*9=81