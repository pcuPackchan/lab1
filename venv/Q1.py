#문제 1~3번

def sum(A):
        b = 0
        for x in range(A+1):
            b = b+x
        return b

def sum2(A):
        b = 0
        for x in range(A+1):
            if x%2 == 0:
                b = b+x
        return b

def factorial(A):
        b = 1
        for x in range(A):
            b = b*(x+1)
        return b

a = input("자연수를 입력해주세요 : ")
print("1부터 {}까지의 합은 {}입니다.".format(int(a),sum(int(a))))
b = input("자연수를 입력해주세요 : ")
print("1부터 {}까지의 짝수의 합은 {}입니다.".format(int(b),sum2(int(b))))
c = input("자연수를 입력해주세요 : ")
print("{}!의 값은 {}입니다.".format(int(c),factorial(int(c))))