    # =-=-=-=-=-=-=-=　#
    #  独自関数の練習   #
    # =-=-=-=-=-=-=-=　#

"""
     ------   問題解説   -------
数値のリストを入力とし、返り値を、各要素の２乗を
足し算した合計とする。たとえば、
[2,3]が入力の場合、返り値は
2^2 + 3^3 => 13となる。関数名は
sum_of_squaresとし、named argのnumbersを利用する。
numbersのデフォルト値は空リスト[]とし、そのままの入力の
場合は、返り値を0とする。
"""

def sum_of_squares(numbers = []):
    result = 0
    # ここに関数の振る舞いを書いてください。
    return result

# 関数をテスト
print(sum_of_squares([])) # "0"
print(sum_of_squares([2,2])) # "8"
print(sum_of_squares([1,2,3,4,5])) # "55"

# ---

def test():
    numbers = [1,2,3,4,5]
    found = sum_of_squares(numbers)
    expected = 55
    if found == expected:
        print(f"""正解です。
入力：{numbers}
f"出力：{found}""")
    else:
        print(f"""
残念でした。もう一度チャレンジしましょう。
今回の要求出力は「{expected}」でしたが、「{found}」が出力されました。
                """)

"""
Correct answer:
    for num in numbers:
        result += num ** 2
"""

test()
