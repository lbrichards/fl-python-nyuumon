# =-=-=-=-=-=-=-=　#
#  タプルの練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
数値のタプルを入力とし、全要素の積を返す。
たとえば、入力が(10,4)の場合、正解は40になる。
"""


def product(tup):
    ...

# 使用例
t = (33,44,55)
p = product(t)
print("The product is:", p)

# ---

def f(t):
    result = 1
    for x in t:
        result *= x
    return result


def test():
    test_tuples = [
        (1,2,3),
        (11,22,33),
        (1,1,2,3,5,8),
        tuple([2**n for n in range(8)])
    ]

    for tup in test_tuples:
        found = product(tup)
        expected = f(tup)
        if found == expected:
            print(f"""正解です。
    入力：{tup}
    出力：{found}""")
        else:
            print(f"""
残念でした。もう一度チャレンジしましょう。
入力の{tup}に対しての
要求出力は「{expected}」でしたが、「{found}」が出力されました。
                    """)


test()
