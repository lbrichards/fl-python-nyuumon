# =-=-=-=-=-=-=-=　#
#  内包表現の練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
下記にkanji_listという漢字のリストがあります。一つの漢字が重複して入っている場合ばあります。
セットを使用した辞書の内包表現により、各漢字の数を示す辞書を生成してください。
"""

kanji_list = ['日', '月', '火', '水', '木', '金', '土', '日', '月', '火']

def make_unique_counts():
    return {} # ここに一行の内包表現を書いてください。

# 使用例
from pprint import pprint
pprint(make_unique_counts())


# ---

def f():
    return {kanji: kanji_list.count(kanji) for kanji in set(kanji_list)}

def test():
    from pprint import pprint
    expected = f()
    found = make_unique_counts()
    if found == expected:
        print("正解です")
        pprint(found)
    else:
        print("残念でした。もう一度チャレンジしましょう")

test()
