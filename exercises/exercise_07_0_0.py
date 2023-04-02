# =-=-=-=-=-=-=-=　#
#  タプルの練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
文字列を入力とするcount_uniqueという関数を書きましょう。
返り値は、その文字列におけるユニークな単語の数とする。set
の要素に重複がないことを利用して、ユニークな（重複しない）単語
のセットを作ることがポイント。下記のtextとう文字列を
テスト入力としよう。
"""
text = """Dolor dolor aliquam aliquam porro dolore magnam ipsum. Sed quiquia 
dolore modi tempora dolore sit quaerat. Eius sed ipsum magnam porro 
ut. Porro aliquam ut consectetur adipisci quiquia dolor. Magnam dolor 
magnam quisquam. Velit velit neque neque est. Non velit ut dolore 
numquam tempora. Quisquam quiquia non magnam ipsum voluptatem quaerat. 
Voluptatem consectetur magnam amet non dolorem quisquam. Etincidunt 
eius amet velit tempora magnam etincidunt.  Neque etincidunt porro 
aliquam porro aliquam consectetur. Velit tempora dolor modi. Porro 
adipisci porro magnam labore aliquam neque eius. Dolor neque magnam 
neque ipsum sed dolore numquam. Quiquia dolor dolorem dolore. 
Ipsum dolor etincidunt eius sed aliquam eius voluptatem. 
Quaerat sed dolorem labore non. Amet porro neque dolorem numquam 
consectetur. Tempora ipsum modi consectetur adipisci. Velit modi 
dolor quisquam quiquia non.  Adipisci labore quaerat adipisci 
quiquia numquam numquam. Adipisci dolor numquam etincidunt amet 
numquam ipsum. Aliquam adipisci sed sit dolor tempora amet non. 
Aliquam est dolor amet porro. Velit dolorem etincidunt porro non. 
Voluptatem sed amet etincidunt neque consectetur. Non ipsum eius 
etincidunt voluptatem tempora voluptatem eius. Numquam velit dolorem 
quiquia. Voluptatem velit porro voluptatem quaerat tempora consectetur. 
Quaerat quaerat adipisci ipsum non adipisci magnam.  Ut non dolorem 
labore. Non modi numquam sed. Non velit tempora sit modi. Adipisci 
adipisci sed velit ipsum. Non sit quisquam consectetur tempora 
aliquam aliquam voluptatem."""



def count_unique(s):
    ... # ここに実装してください

# 使用例
n = count_unique(text)
print("The number of unique words is:", n)

# ---

def f(s):
    return len(set(s.split()))


def test():
    found = count_unique(text)
    expected = f(text)
    if found == expected:
        print(f"""正解です。出力：{found}""")
    else:
            print(f"""
残念でした。もう一度チャレンジしましょう。
要求出力は「{expected}」でしたが、「{found}」が出力されました。
                    """)


test()
