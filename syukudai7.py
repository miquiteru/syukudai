while 1:
    tigau = 0
    suu = int(input("判定したい数字："))
    warusu = list(range(2, int(suu ** 0.5) + 1))
    if suu == 1 or suu == 0:
        print(str(suu) + "は素数ではありません")
        tigau = 1
    for i in warusu:
        if suu % i == 0:
            print(str(suu) + "は素数ではありません")
            tigau = 1
            break
    if tigau == 0:
        print(str(suu) + "は素数です")
    print("")

#２～平方根までの整数のすべてで割り切れないものが素数