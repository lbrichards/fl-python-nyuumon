import platform
if platform.system() == 'Emscripten':
    import matplotlib
    matplotlib.use("module://matplotlib.backends.html5_canvas_backend")
# 　上記のコードを変更しないでください。Codeletの中でmatplotlibを使うのに必要です。

"""
次に、少し芽生えよく加工してみましょう。
"""

from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'MS Gothic'

x = [0, 1]
y = [1, 0]
# 線の色を"g"（グリーン）にしていする。
# lwという引数により線の幅が変えられる。ここで3に設定する。
plt.plot(x, y, 'g', lw=3)
# gridを表示させる
plt.grid(True)
# タイトルを表示させる
plt.title("日本語", font="MS Gothic")

plt.show()
