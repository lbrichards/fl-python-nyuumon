data = [
    [12, 34, 56, 78, 90],
    [23, 45, 67, 89, 12],
    [34, 56, 78, 90, 23],
    [45, 67, 89, 12, 34]
]
def calc_averages():
    num_cols = len(data[0]) # Assumes that all rows have the same number of columns
    # Initialize a list to store the sum of values in each column
    col_sums = [0] * num_cols

    # Iterate over each row and accumulate the sum of values in each column
    for row in data:
        for i, value in enumerate(row):
            col_sums[i] += value

    # Compute the average of values in each column and print the result
    averages = []
    for i, col_sum in enumerate(col_sums):
        averages.append(col_sum / len(data))
    return averages

if __name__ == '__main__':
    print(calc_averages())