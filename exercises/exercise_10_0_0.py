"""
datetimeモジュール、dateutil.parser.parse関数を使用して、
2つの日付の間の日数を求めるプログラムを作成してください。二つの
日数がマイナスにならないように心がけてください。つまり、低い日付と
高い日付を入力する順番に依存しないようにする。


プログラムは、ユーザーに2つの日付を入力するように促し、それらの日付の間の日数をコンソールに出力します。
"""
import datetime
from dateutil.parser import parse

def how_many_days_between(date1_str, date2_str):
    # 文字列からdatetime.dateオブジェクトを作る
    date1 = parse(date1_str).date()
    date2 = parse(date2_str).date()
    return abs((date2-date1).days)

def main():
    # Prompt the user for the two dates
    date1_str = input("Enter the first date in YYYY-MM-DD format: ")
    date2_str = input("Enter the second date in YYYY-MM-DD format: ")
    ndays = how_many_days_between(date1_str, date2_str)
    print(f"There are {ndays} days between {date1_str} and {date2_str}.")


# ---
def test():
    s2 = '2025-03-11'
    s1 = '2026-03-11'
    test_output = how_many_days_between(s1, s2)
    correct_answer = 365
    if test_output == correct_answer:
        print(f"正解です。出力：{test_output}")
    else:
        print(f"""
        残念でした。もう一度チャレンジしましょう。
        今回の要求出力は「{correct_answer}」でしたが、「{test_output}」が出力されました。
        """)


# call the test function
test()
