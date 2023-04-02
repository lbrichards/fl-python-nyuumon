# =-=-=-=-=-=-=-=　#
#  セットの練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
下記に３つのセットを入力とするsummarize(a,b)という関数
を書きましょう。次の二つの新しいセットを返り値とする。

(set1とset2の和集合, set1とset2共通部分) (setのtuple)
"""

set1 = {"carbon", "hydrogen", "oxygen", "nitrogen", "phosphorus"}
set2 = {"oxygen", "nitrogen", "chlorine", "sulfur", "iron"}

def summarize(a,b):
    return set(), set() # ここに実装してください

# 使用例
union, intersection = summarize(set1,set2)
print("The union is:", union)
print("The intersection is:", intersection)


# ---

def f(a, b):
    return a | b, a & b


def test():
    found = summarize(set1, set2)
    expected = f(set1, set2)
    if found == expected:
        print(f"""正解です。出力：{found}""")
    else:
            print(f"""
残念でした。もう一度チャレンジしましょう。
要求出力は「{expected}」でしたが、「{found}」が出力されました。
                    """)


test()
