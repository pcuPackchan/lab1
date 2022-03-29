
a = input("온도를 입력해주세요. : ")
b = input("변환을 원하는 온도(화씨=F,섭씨=C)를 입력해주세요. : ")

if b=="F":
    c = (9/5)*float(a)+32
    print("{:10.1f} C = {:10.1f} F 입니다.".format(float(a),float(c)))
else:
    c = (5/9)*(float(a)-32)
    print("{:10.1f} F = {:10.1f} C 입니다.".format(float(a),float(c)))