import numpy
data = [
    [12, 34, 56, 78, 90],
    [23, 45, 67, 89, 12],
    [34, 56, 78, 90, 23],
    [45, 67, 89, 12, 34]
]
def calc_averages():
    return list(numpy.array(data).mean(axis=0))


if __name__ == '__main__':
    print(calc_averages())