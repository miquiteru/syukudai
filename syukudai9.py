while 1:  
    suu = int(input("いくら？"))
    hyaku = suu // 100
    nokori = suu % 100
    zyuu = nokori // 10
    nokori %= 10
    iti = nokori

    print("100円：" + str(hyaku) + "枚")
    print("10円：" + str(zyuu) + "枚")
    print("1円：" + str(iti) + "枚")
    print("")