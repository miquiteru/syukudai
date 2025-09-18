while True:
    wariai = list(map(int, (input("課題、中間、定期の評価割合：")).split(",")))
    manten = list(map(int, (input("それぞれの満点の点数：")).split(",")))
    tokuten = list(map(int, (input("それぞれの獲得した点数：")).split(",")))
    kizyunti = list(map(int, (input("A,B,C,Fの基準値：")).split(",")))
    hyoukaten = 0
    for i in range(3):
        hyoukaten += tokuten[i] * wariai[i] / 100
    if hyoukaten >= kizyunti[0]:
        print("単位：A")
    elif hyoukaten < kizyunti[0] and hyoukaten >= kizyunti[1]:
        print("単位：B")
    elif hyoukaten < kizyunti[1] and hyoukaten >= kizyunti[2]:
        print("単位：C")
    else:
        print("単位：F")
    print("")