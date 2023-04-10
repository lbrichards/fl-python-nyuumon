data = [
    [12, 34, 56, 78, 90],
    [23, 45, 67, 89, 12],
    [34, 56, 78, 90, 23],
    [45, 67, 89, 12, 34]
]
def calc_averages():
    num_cols = len(data[0]) # 正解例
    col_sums = [0] * num_cols # 正解例
    for row in data: # 正解例
        for i, value in enumerate(row): # 正解例
            col_sums[i] += value # 正解例
    averages = [] # 正解例
    for i, col_sum in enumerate(col_sums): # 正解例
        averages.append(col_sum / len(data)) # 正解例
    return averages # 正解例

# ---

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

exercise_test()