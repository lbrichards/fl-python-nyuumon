import platform
if platform.system() == 'Emscripten':
    import matplotlib
    matplotlib.use("module://matplotlib.backends.html5_canvas_backend")
from matplotlib import pyplot as plt
plt.clf()
# 　上記のコードを変更しないでください。Codeletの中でmatplotlibを使うのに必要です。

"""
面積塗りつぶしプロットをつくってみよう。
先ほどのベル関数を元に、特定の部分とy=0の横線の間を
塗りつぶす。この場合はplt.fill_between()関数が便利です。

主な引数は...
    x : 横軸の変数
    y1 : 塗りつぶしの上限
    y2 : 塗りつぶしの下限
    where : 塗りつぶしエリアを限定する条件
    color : 塗りつぶし色の名前（文字列）
    alpha : 0から１の透明度(float)
"""
import numpy
from matplotlib import pyplot as plt
x = numpy.linspace(-3,3,200)
y = numpy.exp(x**2)**-.5
plt.plot(x, y, 'k', label="f(x)")
plt.fill_between(
    x, y1 = y, y2 = 0, where = (x>1) | (x<-1) , color = 'g', alpha=.3)

plt.grid(True)
plt.title("f(x)")
plt.legend()
plt.show()

"""
演習：次のようにグラフを変えてみてください。
    where の条件文を色々変えてみる
    colorを変えてみる
    alphaを変えてみる
"""
