"""
dataという二重リストには、４行と５列がああります。
各列の平均値を計算するcalc_averages()という関数を
実装してください。返り値として５つの値のリストとする。
"""


data = [
    [12, 34, 56, 78, 90],
    [23, 45, 67, 89, 12],
    [34, 56, 78, 90, 23],
    [45, 67, 89, 12, 34]
]

def calc_averages():
    averages = [] #ここを変更してください
    return averages

# ---


locals()["__istest__"] = False
def test():
    locals()["__istest__"] = True

if __istest__:

def exercise_test():
    from numpy import testing
    test_output = calc_averages()
    correct = [28.5, 50.5, 72.5, 67.25, 39.75]
    try:
        testing.assert_array_equal(test_output, correct)
        print(f"正解です。出力：{test_output}")
    except:
        print(f"""
残念でした。もう一度チャレンジしましょう。
今回の要求出力は「{correct}」でしたが、「{test_output}」が出力されました。
    """)

if locals['__istest__']:
    exercise_test()
else:
    calc_averages()


