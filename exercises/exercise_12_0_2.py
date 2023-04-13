import platform
if platform.system() == 'Emscripten':
    import matplotlib
    matplotlib.use("module://matplotlib.backends.html5_canvas_backend")
from matplotlib import pyplot as plt
plt.clf()
# 　上記のコードを変更しないでください。Codeletの中でmatplotlibを使うのに必要です。

"""
次に、いろいろな曲線を描いてみよう。
そのために、numpyという数学ライブラリーが便利です。
"""
import numpy
from matplotlib import pyplot as plt
# linspace(a,b,n)という関数により、
# aからbまでの区間をnの均等分割したアレーを作ります。
x = numpy.linspace(-3,3,200)
#　numpy arrayの計算は、普通の数値（スカラー）と同じように書きますが
y = 4 * x ** 3 + x ** 2
#  結果のyも、numpy arrayになります。
plt.plot(x, y, 'k', label="f(x)")
plt.grid(True)
plt.title("f(x)")
plt.legend()
plt.show()

"""
演習：次のようにグラフを変えてみてください。
yの式をいろいろ変えてみる。
例えば、
    y=numpy.sin(x) とか
    y=x**2 とか
    y=numpy.exp(x) とか
    y = numpy.exp(x**2)**-.5 とか
    ...
"""
