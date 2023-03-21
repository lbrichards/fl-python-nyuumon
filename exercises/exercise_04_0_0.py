
zoo_animals = [
    "monkey", "turtle", "giraffe",
    "tiger", "peacock", "polar bear", "panda",
    "reindeer"
]

maybe_in_zoo = [
    "turkey", "snake", "elephant", "cow", "horse",
    "goat", "eagle", "panda", "rabbit", "rhino"
]


def return_first_zoo_animal():
    for animal in maybe_in_zoo:
        ... # この行を消す
        # ここを変更してください
        # zooに入っているanimalが
        # 見つかったらループを中断させる。

    return animal

# ---

def test_return_first_zoo_animal():
    found = return_first_zoo_animal()
    expected = "panda"
    if found == expected:
        print(f"正解です。出力：{found}")
    else:
        print(f"""
残念でした。もう一度チャレンジしましょう。
今回の要求出力は「{found}」でしたが、「{expected}」が出力されました。
                """)

test_return_first_zoo_animal()