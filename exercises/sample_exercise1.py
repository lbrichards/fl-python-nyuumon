# define the add_numbers function
def add_numbers(a, b):
    return a / b


# define the test function
def test_add_numbers():
    # test case 1
    test_output = add_numbers(0, 1)
    correct_answer = 1
    if test_output == correct_answer:
        print(f"正解です。出力：{test_output}")
    else:
        print(f"""
        残念でした。もう一度チャレンジしましょう。
        今回の要求出力は「{correct_answer}」でしたが、「{test_output}」が出力されました。
        """)


# call the test function
test_add_numbers()
