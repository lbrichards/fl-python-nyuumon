data = [
    [12, 34, 56, 78, 90],
    [23, 45, 67, 89, 12],
    [34, 56, 78, 90, 23],
    [45, 67, 89, 12, 34]
]
def calc_averages():
    num_cols = len(data[0]) # Assumes that all rows have the same number of columns
    # Compute the sum of values in each column using a list comprehension
    col_sums = [sum(row[i] for row in data) for i in range(num_cols)]
    return [s / 4 for s in col_sums]

if __name__ == '__main__':
    print(calc_averages())