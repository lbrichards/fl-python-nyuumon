    # =-=-=-=-=-=-=-=　#
    #  独自関数の練習   #
    # =-=-=-=-=-=-=-=　#

"""
     ------   問題解説   -------
itertoolsモジュールには、効率的なループ実行のためのイテレータ生成関数を
たくさん提供しています。
本演習問題では、itertools中の
combinations_with_replacement()という関数を利用します。

利用例：

>>> list(combinations_with_replacement('ABC', r=2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

見てわかるように、'ABC'の各要素を、（重複ありで）２個ずつ取り出し、
可能な組み合わせを全て羅列します。*

*この場合は組み合わせが見えるようにlist()で包んでいます。listを使わなかったら
返り値はイテレーター・オブジェクトですから、その場合は中身が見えなかったからです。

注意点　ー　引数の"r"を大きく設定すると、夥しいコンビネーションが生成され、
演算時間が非常に長くなることもあります。ご注意ください。

さて、今回の演習問題のです。レジの中に次の六種類の硬貨が１００個ずつ入っているとします。

一円
五円
十円
五十円
百円
五百円

レジの中から、15個の硬貨が一辺に取り出すことが可能です。
２０個の合計金額がちょうど千円になるようなる、コンビネーションを
全てリストにしてください。返り値はリストのリストになります。

ヒント：コンビネーションの合計を確認するのにsum()関数を使うと便利です。
例えば、sum([1,5,10,50]) => 66になります。
"""
from itertools import combinations_with_replacement

coin_list = [1, 5, 10, 50, 100, 500]

def make_1000_yen_combinations():
    sums_to_1000 = []
    #　ここに関数のロジックを実装してください
    return sums_to_1000

# テスト　プログラム
combs = make_1000_yen_combinations()
for c in combs:
    print(c)

# ---

def f():
    sums_to_1000 = []
    for combination in combinations_with_replacement(coin_list,15):
        if sum(combination)==1000:
            sums_to_1000.append(combination)
    return sums_to_1000
def test():
    L = 1.5
    epsilon = 1e-10
    found = make_1000_yen_combinations()
    expected = f()
    if found == expected:
        print(f"正解です。出力：")
        for l in expected:
            print(l)
    else:
        print(f"""
残念でした。もう一度チャレンジしましょう。
次の誤った返り値が出力されました。
                """)
        if len(found) and type(found)==list:
            for l in found:
                print(l)
        else:
            print(found)

test()
