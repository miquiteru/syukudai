while True:
    while True:
        suu = list(map(int, input("数字を入力：").split(',')))
        if len(suu) == 2:
            break
    enzan = input("演算子を入力：")
    gokei = suu[0]
    if enzan == "+":
            gokei += suu[1]
    elif enzan == "-":
            gokei -= suu[1]
    elif enzan == "*":
            gokei *= suu[1]
    elif enzan == "%":
            gokei %= suu[1]
    elif enzan == "^":
            gokei ^= suu[1]
    else:
            gokei /= suu[1]
    print("演算結果：" + str(gokei))
    print("")