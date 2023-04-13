import platform
if platform.system() == 'Emscripten':
    import matplotlib
    matplotlib.use("module://matplotlib.backends.html5_canvas_backend")
# 　上記のコードを変更しないでください。Codeletの中でmatplotlibを使うのに必要です。

"""
matplotlibでプロッティングしてみよう！
matplotlibとは、Pythonにおける最も人気が高いプロッティング（可視化）ライブラリーでしょう。
matplotlibでどんなことができるかを見るには、ギャラリーをご覧ください。
https://matplotlib.org/stable/gallery/index.html

ここでは、シンプルな例をご紹介します。まずは、直線です。
"""

# matplotlibのpyplotをpltとしてimportする
from matplotlib import pyplot as plt

# dataを作る
x = [0, 1]
y = [1, 0]

# dataをプロットする
plt.plot(x, y)

# プロットを表示させる
plt.show()
