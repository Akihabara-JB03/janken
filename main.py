import random

def janken(user_hand):
    ai_te = random.randint(0,2)
    if user_hand == ai_te:
        print("次が勝負ですね！！")
    elif (user_hand - ai_te + 3) % 3 == 2:
        print("僕の負けか～！！次だ次！！")
    else:
        print("僕の勝ちだ！！ふぇえ～～い！！")