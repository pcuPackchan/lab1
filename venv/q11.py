import sys

try:
    filename = input("열람할 파일 이름을 지정해주세요:")
    myFile = open(filename,"r")
    a=1
    line = myFile.readline()
    while line:
        print("{}: {}".format(a,line))
        line = myFile.readline()
        a += 1
    myFile.close()
except:
    error = sys.exc_info()[0]
    print("!!File Not Found Error!!")
else:
    print("열람이 종료되었습니다.")
finally:
    print("종료합니다.")