

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
from tkinter import N
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


#素数を求める ----------------------------------
def isPrimeNum (max):
    for i in range(2, max):
        h = i//2  #iの半分の値で素数かチェック
        f = True

        # print("{}-{}".format(i, h))
        print(h+1)

        #h+1までの範囲を割り切れるかチェック
        for j in range(2, h+1):
            if i%j == 0:
                f = False
                break
        #割り切れたら素数として出力
        if f == True:
            print(i, end=",")
isPrimeNum(10)

#階乗を求める --------------------------------
#n*n-1*n-2.....
def getFactorial(max):
    r = 1
    for i in range(2, max+1):
        r = r*i

    print("{}!={}".format(max,r))

getFactorial(10)
getFactorial(5)


#再帰関数
def recursion(n):
    if (n == 0) or (n < 0):
        print("処理終了")
    else:
        print(n, end=",")
        n = recursion(n-1)
r =recursion(10)

#偶数奇数判定
def EvenOrAdd (list):
    for i in range(len(list)):
        n = list[i]
        str = "奇数"
        if n % 2 == 0:
            str = "偶数"
        print("{} = {}".format(n,str))


list = [10,-5,0,29,6,2,77,8]
EvenOrAdd(list)


# #エラトステネスの篩 -------------------------------------
# #素数の効率的な求め方
# #2,3,4,5....11までの倍数をチェック
# p = [True]*100 #100個のTrueリストを生成
# p[0] = False #0は対象外
# p[1] = False #1は対象外
# n = 2 #素数チェックの初期値

# #0 - 99までのリストを生成
# def hyou ():
#     s = ""
#     for i in range (100):
#         if p[i] == True:
#             s += "{:2d}, ".format(i)
#         else:
#             s += "/, "
#         if i%10 == 9:
#             s += "\n"
#     print(s)

# #hyouで生成したリストから倍数毎の値をFalse化
# #倍数は3,4,5,7
# def furui():
#     global n
#     for i in range(n+n, 100, n):
#         p[i] = False
#     print(n, "の倍数をふるい落としました。")
#     hyou()
#     while n<100:
#         n = n + 1
#         if p[n] == True:
#             break

# hyou() #リスト生成
# while n<10:
#     input("エンターキーを押して下さい")
#     furui()


#スタック --------------------------------------------
#後入れ先出しの考え方を持つデータ構造

MAX   = 5 #最大値
stack = [0]*MAX #リスト化
sp = 0 #スタックポインタ

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("データ[", d, "]を追加しました。")
    else:
        print("スタックは一杯です。これ以上追加できません。")

def pop():
    global sp
    if sp > 0:
        sp = sp - 1
        return stack[sp]
    else:
        print("取り出すデータが存在しません。")
        return None

#pushのループ
for i in range(6):
    push(i)
#popのループ
for i in range(6):
    v = pop()
    print("取り出したデータ", v)




#キュー --------------------------------------------
#先入れ先出しのデータ構造
#データ追加をenqueue、データ取り出しをdequeueという

MAX   = 7 #最大値
que = [0]*MAX #リスト化
head = 0 #データ取り出し位置
tail = 0 #データ登録位置

def enqueue(d):
    global tail
    nt = (tail+1)%MAX
    if nt == head:
        print("これ以上データ追加できません。")
    else:
        que[tail] = d
        tail = nt
        print("データ", d, "を追加しました。")

def dequeue():
    global head
    if head == tail:
        print("取り出すデータが存在しません")
        return None
    else:
        d = que[head]
        head = (head+1)%MAX
        return d

#enqueueのループ
for i in range(7):
    enqueue(i)
print(que)
#dequeueのループ
for i in range(7):
    v = dequeue()
    print("取り出したデータ", v)
print(que)



#線形リストの追加、削除、一覧表示 ------------------------
MAX     = 5
data    = [None]*MAX
pointer = [None]*MAX
head    = 0

#リストにデータを追加
def add_list(d):
    n = -1 #処理リセット値
    #配列内の空きを探す
    for i in range(MAX):
        if data[i] == None:
            n = i
            break
    #空きなしで抜ける
    if n == -1:
        print("データ領域に空きがありません")
        return False
    #最後尾のノードを探す
    for i in range(MAX):
        if data[i] != None and pointer[i] == None:
            pointer[i] = n
            break
    #ポインタ、データをセット
    data[n]    = d
    pointer[n] = None
    print("データ", d, "を追加しました")
    return True

def del_list(d):
    global head
    n = -1 #処理リセット値
    #配列内に一致するデータを探す
    for i in range(MAX):
        if data[i] == d:
            n = i
            break
    if n == -1:
        print("そのデータは存在しません")
        return False
    if n == head:
        #ポインタの値をheadにセット
        head = pointer[n]
        #データが1個かつ、それを削除した場合はheadを先頭（0）に戻す
        if head == None:
            head = 0
    else:
        #ポインタとheadが一致しない場合は付け替える
        for i in range(MAX):
            if pointer[i] == n:
                pointer[i] = pointer[n]
    data[n]    = None
    pointer[n] = None
    print("データ", d, "を削除しました")
    return True

def put_list():
    p = head
    while True:
        print(data[p], end="→")
        if pointer[p] == None:
            print("EOF")
            break
        p = pointer[p]

for i in range(10, 70, 10):
    add_list(i)
del_list(10)
del_list(20)
put_list()

