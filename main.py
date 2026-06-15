import random
aiko,kati,make = 0,0,0
def janken(user_hand):
    global aiko,make,kati
    ai_te = random.randint(0,2)
    
    if user_hand == ai_te:
        print("次が勝負ですね！！")
        aiko+=1
    elif (user_hand - ai_te + 3) % 3 == 2:
        print("僕の負けか～！！次だ次！！")
        kati+=1
    else:
        print("僕の勝ちだ！！ふぇえ～～い！！")
        make+=1
    print(f"勝ち:{kati}回　負け:{make}回 あいこ:{aiko}回")