while True:
    nenri = int(input("年利％："))
    syokizyoge = list(map(int, (input("初期値、上限値：")).split(",")))
    tyokin = syokizyoge[0]
    nensu = 0
    while tyokin <= syokizyoge[1]:
        tyokin += tyokin * nenri / 100
        nensu += 1
    print("かかった年：" + str(nensu)) 
    print("")