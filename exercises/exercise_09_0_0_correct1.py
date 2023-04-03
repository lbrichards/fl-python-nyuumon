# =-=-=-=-=-=-=-=　#
#  内包表現の練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
inlistを入力とし、各要素を２で掛け算した
新しいリストを出力する関数を書きましょう。
リストの内包表現を使うようにしてください。
"""

def multiply_each_by_2(inlist):
    return [x*2 for x in inlist] # 正解例

# 使用例
list1 = [3,6,9]
list2 = multiply_each_by_2(list1)
print("The result is :", list2)

# ---

def f(l):
    return [x*2 for x in l]


test_inputs = [
    [3,6,9],
    [5,10,15],
    [ 23, 29, 31, 37],
    [103, 107, 109, 113],
    ['ラン', 'リン', 'シン','シャン','ユウ']
]
def test():
    for i, inlist in enumerate(test_inputs):
        found = multiply_each_by_2(inlist)
        expected = f(inlist)
        if found == expected:
            print(
                f"""Test Case {i+1}:
正解です。入力の
{inlist}に対して、
{found}が出力されました。""")
        else:
            print(f"""
残念でした。もう一度チャレンジしましょう。
「入力の{inlist}に対して、{expected}が出力されるよていでしたが
今回の出力は{found}でした。
""")
            break


test()
