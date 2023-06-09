# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# while loopの練習問題 #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

"""
     ------   問題解説   -------
数列を使って黄金比に近づこう！　（近似値を求める）

下記のwhile loopの中で、黄金比の近似値が計算されるように
なっています。反復するほど、ratioの変数が黄金比に近づいて
いきます。そして、ratioとprev_ratioの差分が小さくなって
いきます。ratioとprev_ratioの差分がtoleranceより小さく
なったら、ループをとめてratioを返すようにしてください。

"""

tolerance = 1e-12

def calc_golden_ratio():
    a, b = 1, 2
    prev_ratio = tolerance
    ratio = b

    while abs(ratio - prev_ratio) > tolerance: # 正解例
        a, b = b, a + b
        prev_ratio, ratio = ratio, b / a
    return ratio

print(calc_golden_ratio())


# ---

def test():
    from math import sqrt
    expected = (1 + sqrt(5)) / 2
    found = calc_golden_ratio()

    if abs(expected - found) <= tolerance:
        print(f"正解です。出力：{found}")
    else:
        print(f"""
残念でした。もう一度チャレンジしましょう。
今回の要求出力は「{expected}」でしたが、「{found}」が出力されました。
                """)

test()