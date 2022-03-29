import math

a = float(input("구의 반지름을 입력해주세요."))

S = 4*math.pi*math.pow(a,2)
V = (4/3)*math.pi*math.pow(a,3)
print("구의 겉면적은 {},부피는 {}입니다.".format(S,V))