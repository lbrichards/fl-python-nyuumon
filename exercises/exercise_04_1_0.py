# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# for loopでcontinueを利用する練習問題 #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

"""
     ------   問題解説   -------

以下に、uncommon_wordsというリストがある。その中から"n"を含まない
要素のみのリストを作ることが目標です。回答に必ずcontinueを
使ってください。
"""

uncommon_words = [
    'obfuscate', 'quixotic', 'surreptitious',
    'sesquipedalian', 'lackadaisical', 'insouciant',
    'effervescent', 'perspicacious', 'ebullient',
    'recalcitrant', 'jejune', 'pulchritudinous',
    'coruscate', 'defenestration', 'susurrus', 'lagniappe',
    'discombobulate', 'lilliputian', 'macrosmatic', 'nidificate']


def get_words_without_letter_n():
    without_n = []
    for word in uncommon_words:
        # ここに回答を書いてください。
        without_n.append(word)
    return without_n

print(get_words_without_letter_n())



# ---

def test():
    expected = [w for w in uncommon_words if 'n' not in w]
    found = get_words_without_letter_n()

    if set(found) == set(expected):
        print(f"正解です。出力：{found}")
    else:
        print(f"""
残念でした。もう一度チャレンジしましょう。
今回の要求出力は「{expected}」でしたが、「{found}」が出力されました。
                """)

test()