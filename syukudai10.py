import random
while 1:
    kotae = random.randint(1, 500)
    kaisu = 0
    yoso = 0
    while kotae != yoso:
        yoso = int(input("数を入力："))
        kaisu += 1
        if yoso < kotae:
            print("それよりおおきい")
        elif yoso > kotae:
            print("それよりちいさい")
    print(str(kaisu) + "で正解しました！")
    print("")