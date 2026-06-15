import random
aiko,kati,make,siai_kaisu,syouritu = 0,0,0,0,0
def janken(user_hand):
    global aiko,make,kati,siai_kaisu,syouritu
    ai_te = random.randint(0,2)
    siai_kaisu+=1
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
    syouritu = kati / siai_kaisu
    print(f"あなたの勝率は、{syouritu*100}%です")
    if syouritu*100 > 95:
        print("いいな～！羨ましいな～")
    elif syouritu*100 <= 95 and syouritu*100 > 74:
        print("すごいね～。")
    else:
        print("運が悪いんですね～")
    
    print("これでも、130~140KiBを維持しているんですよ。流石C言語！！")