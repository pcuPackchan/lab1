import random
def randQ():
    a = str(random.randint(1, 9))
    b = str(random.randint(1, 9))
    ans = str(a)
    ans = ans + '*'
    ans = ans + str(b)

    return ans

cor = 0
wro = 0
while True:
    Q = randQ()
    print(Q)
    c = int(input("= "))
    if c==eval(Q):
        print("정답입니다.")
        cor = cor+1
    else:
        print("오답입니다.")
        wro = wro+1
    sys = input("계속 하시겠습니까?\n중단을 원한다면 exit를 입력해주세요.: ")
    if sys=="exit":
        break
    else:
        print("진행합니다.")
if cor==0:
    print("모든 문제를 틀렸습니다.")
else:
    res = cor/(cor+wro)
    print("정답률은 {}%입니다.".format(float(res*100)))