while 1:
    koko = int(input("何番まで表示する？"))
    for i in range(koko):
        suu = i + 1
        if suu >= 15 and suu % 15 == 0:
            print("hogefuga")
        elif suu >= 3 and suu % 3 == 0:
            print("hoge")
        elif suu >=5 and suu % 5 == 0:
            print("fuga")
        else:
            print(str(suu))
    print("")