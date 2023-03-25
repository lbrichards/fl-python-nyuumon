    # =-=-=-=-=-=-=-=　#
    #  独自関数の練習   #
    # =-=-=-=-=-=-=-=　#

"""
     ------   問題解説   -------
振り子長さを入力として振り子の周波数を返す関数を書きましょう。
長さ(m)をLと書いた場合、周波数fは次の式で求められます。fの単位はHzです。

f = 1/(2π) √(g/L)

gは重力加速度（m/s^2）の定数です
"""

from math import pi, sqrt
g = 9.8

def calc_frequency(L):
    return #ここで戻り値を計算

# 関数をテスト
L = 1.5
f = calc_frequency(L)
print(f"A pendulum with length {L} meters has a frequency of {f:0.2f} Hz")


# ---

def test():
    L = 1.5
    epsilon = 1e-10
    found = calc_frequency(L)
    expected = 1/(2*pi) * sqrt(g * L)
    if found - expected < epsilon:
        print(f"正解です。出力：{found}")
    else:
        print(f"""
残念でした。もう一度チャレンジしましょう。
今回の要求出力は「{expected}」でしたが、「{found}」が出力されました。
                """)

test()
