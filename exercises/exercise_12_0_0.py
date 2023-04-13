import platform
if platform.system() == 'Emscripten':
    import matplotlib
    matplotlib.use("module://matplotlib.backends.html5_canvas_backend")

from matplotlib import pyplot as plt
x = [v/100 for v in range(-10, 11)]
y = [v**2 for v in x]
plt.plot(x,y)
plt.show()