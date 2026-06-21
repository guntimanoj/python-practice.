import numpy as np


def basic_indexing_demo():
    arr = np.array([10, 20, 30, 40, 50])
    print("Array:", arr)
    print("First element:", arr[0])
    print("Last element:", arr[-1])
    print("Slice [1:4]:", arr[1:4])
    print("Every other element:", arr[::2])


def reshaping_demo():
    arr = np.arange(1, 13)  # 1..12
    print("\nOriginal (1D):", arr)

    reshaped_3x4 = arr.reshape(3, 4)
    print("Reshaped to 3x4:\n", reshaped_3x4)

    reshaped_2x6 = arr.reshape(2, 6)
    print("Reshaped to 2x6:\n", reshaped_2x6)

    flattened = reshaped_3x4.flatten()
    print("Flattened back to 1D:", flattened)


def boolean_indexing_demo():
    arr = np.array([4, -2, 7, -9, 0, 15, -3])
    print("\nArray:", arr)
    print("Positive values:", arr[arr > 0])
    print("Negative values:", arr[arr < 0])

    arr_copy = arr.copy()
    arr_copy[arr_copy < 0] = 0
    print("Negatives replaced with 0:", arr_copy)


def two_d_slicing_demo():
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    print("\nMatrix:\n", matrix)
    print("Row 1:", matrix[1])
    print("Column 2:", matrix[:, 2])
    print("Top-left 2x2 block:\n", matrix[:2, :2])


if __name__ == "__main__":
    basic_indexing_demo()
    reshaping_demo()
    boolean_indexing_demo()
    two_d_slicing_demo()