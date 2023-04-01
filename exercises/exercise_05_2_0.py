# =-=-=-=-=-=-=-=　#
#  独自関数の練習   #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
果物の種類を判別する関数を書きましょう。

関数名：classify_fruit
引数：color (str), shape (str)

対象となる果物の特徴：

"apple": color = "red"
    shape = "round"

"orange": color = "orange"
    shape = "round"
    
"banana": color = "yellow"
    shape = "curved"

判別できない場合は"unknown"を返す。
"""


def classify_fruit(color, shape):
    if color == "red" and shape == "round":
        ...


# 使用例
fruit_color = "red"
fruit_shape = "round"
fruit_type = classify_fruit(fruit_color, fruit_shape)
print("This fruit is:", fruit_type)

# ---
from itertools import product


def model(color, shape):
    if color == "red" and shape == "round":
        return "apple"
    elif color == "yellow" and shape == "curved":
        return "banana"
    elif color == "orange" and shape == "round":
        return "orange"
    else:
        return "unknown"


def test():
    colors = ["red", "yellow", "orange"]
    shapes = ["round", "curved"]

    for color, shape in product(colors, shapes):
        found = classify_fruit(color, shape)

        expected = model(color, shape)
        if found == expected:
            print(f"""正解です。
    入力：{(color, shape)}
    出力：{found}""")
        else:
            print(f"""
    残念でした。もう一度チャレンジしましょう。
    今回の要求出力は「{expected}」でしたが、「{found}」が出力されました。
                    """)


test()
