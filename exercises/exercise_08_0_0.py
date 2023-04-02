# =-=-=-=-=-=-=-=　#
#  辞書の練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
下記のmangaという辞書を使用する問題です。
mangaのキーが一致するアイテムを
削除し、変更済みの辞書を返す関数を書いてくださ合い。
元の辞書がそのまま残るように
manga2 = deepcopy(manga)
により、まずコピーを作って、コピーに変更を
加えましょう。
"""
from copy import deepcopy

manga = {
    "One Piece": "Shueisha",
    "Naruto": "Shueisha",
    "Attack on Titan": "Kodansha",
    "Dragon Ball": "Shueisha",
    "Death Note": "Shueisha"
}
def remove_specific_manga(manga_title):
    manga2 = deepcopy(manga)
    # ここに実装してください
    return manga2

# 使用例
manga2 = remove_specific_manga("Naruto")
print("The result is :", manga2)

# ---

def f(k):
    manga2 = deepcopy(manga)
    del manga2[k]
    return manga2

def test():
    for i, to_remove in enumerate(manga.keys()):
        found = remove_specific_manga(to_remove)
        expected = f(to_remove)
        if found == expected:
            print(
                f"""Test Case {i+1}:
正解です。{to_remove}は正しく削除されました。""")
        else:
            print(f"""
残念でした。もう一度チャレンジしましょう。
「{to_remove}」が削除される予定でしたが、
削除されなかったようです。""")
            exit()


test()
