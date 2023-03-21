# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# for loopをbreakで中断する練習問題   #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

"""
     ------   問題解説   -------

以下に、zoo_animalsと、maybe_in_zooという二つのリストがあります。
for loopの中で、maybe_in_zooの中から、zoo_animalsにも含まれる要素を
検出し、ループをbreakにより中断させる。ループを中断すると、その時の
animalとう変数の値が返される。

つまり、今回はget_first_zoo_animal()という関数が、どこかの
プログラムで呼ばれると、その呼ばれたところに返り値を返す。
関数の最後にreturn...というキーワードを入れると、
値を「返り値」として返す働きがあります。returnについては、ここで
特に考える必要はありません。後ほど関数のレッスンで詳しく
勉強します。
"""

zoo_animals = [
    "monkey", "turtle", "giraffe",
    "tiger", "peacock", "polar bear", "panda",
    "reindeer"
]

maybe_in_zoo = [
    "turkey", "snake", "elephant", "cow", "horse",
    "goat", "eagle", "panda", "rabbit", "rhino"
]


def get_first_zoo_animal():
    for animal in maybe_in_zoo:
        ... # この行を消す
        # ここを変更してください
        # zooに入っているanimalが
        # 見つかったらループを中断させる。

    return animal

print(get_first_zoo_animal())

# ---

def test_get_first_zoo_animal():
    found = get_first_zoo_animal()
    expected = "panda"
    if found == expected:
        print(f"正解です。出力：{found}")
    else:
        print(f"""
残念でした。もう一度チャレンジしましょう。
今回の要求出力は「{expected}」でしたが、「{found}」が出力されました。
                """)

test_get_first_zoo_animal()