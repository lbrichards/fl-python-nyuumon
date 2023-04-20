import platform
if platform.system() == 'Emscripten':
    import matplotlib
    matplotlib.use("module://matplotlib.backends.html5_canvas_backend")
from matplotlib import pyplot as plt
plt.clf()
# 　上記のコードを変更しないでください。Codeletの中でmatplotlibを使うのに必要です。

"""
次に、少し見栄えよく加工してみたり、図の属性を色々変えてみよう。
"""

from matplotlib import pyplot as plt
x = [0, 1]
y = [1, 0]
# 線の色を"g"（グリーン）に設定する。
# lwという引数により線の太さが変えられる。
# alphaは0から１の間の、透明度を示すパラメータです。低いほど透明です。
plt.plot(x, y, 'g', lw=10, alpha=.4, label="straight line")
# gridを表示させる
plt.grid(True)
# タイトルを表示させる
plt.title("My first plot")
plt.legend()
plt.show()

"""
演習：次のようにグラフを変えてみてください。
（１）線の色を"g"の別の色に変えてる。
使用可能な色はここにあります。
https://matplotlib.org/stable/gallery/color/named_colors.html
（２）線のalpha値を変えてみる。
（３）線の太さを変えてみる
（４）線のlabelを変えてみる
（５）図のtitleを変えてみる
（６）gridをオフにしてみる
（７）xとyのデータを変えてみる
"""
