while True:
    syurui = (input("図形の種類："))
    if syurui == "1":
        atai = list(map(int, (input("底辺、高さを入力：")).split(",")))
        print(str(atai[0] * atai[1] / 2))
    if syurui == "2":
        atai = list(map(int, (input("縦、横を入力：")).split(",")))
        print(str(atai[0] * atai[1]))
    if syurui == "3":
        atai = list(map(int, (input("上底、下底、高さを入力：")).split(",")))
        print(str((atai[0] + atai[1]) * atai[2] / 2))
    if syurui == "4":
        atai = list(map(int, (input("底辺、高さを入力：")).split(",")))
        print(str(atai[0] * atai[1]))
    if syurui == "5":
        atai = list(map(int, (input("半径を入力：")).split(",")))
        print("約" + str(atai[0] ** 2 * 3.1415))
    if syurui == "6":
        atai = list(map(int, (input("半径、中心角を入力：")).split(",")))
        print("約" + str(atai[0] ** 2 * 3.1415 * atai[1] / 360))
    print("")