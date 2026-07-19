Topic : Mean, Median, Mode in Python
------------------------------------------------------------------
import numpy as np
import statistics
from scipy import stats
from collections import Counter


def my_mean(data):
    """Sum of all values divided by the number of values."""
    return sum(data) / len(data)


def my_median(data):
    """Middle value of sorted data; average of two middles if even length."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2


def my_mode(data):
    """Most frequently occurring value(s). Returns a list (handles multimodal data)."""
    counts = Counter(data)
    max_freq = max(counts.values())
    modes = [value for value, freq in counts.items() if freq == max_freq]
    return sorted(modes)


# ===========================================================
# EXAMPLE 1: Odd-length dataset
# ===========================================================
data1 = [12, 7, 3, 9, 15, 7, 21, 7, 9]

print("=" * 60)
print("Example 1: Odd-length dataset")
print("=" * 60)
print(f"Data: {data1}")
print(f"Mean   (custom) : {my_mean(data1):.4f}")
print(f"Mean   (stdlib) : {statistics.mean(data1):.4f}")
print(f"Mean   (numpy)  : {np.mean(data1):.4f}")

print(f"\nMedian (custom) : {my_median(data1)}")
print(f"Median (stdlib) : {statistics.median(data1)}")
print(f"Median (numpy)  : {np.median(data1)}")

print(f"\nMode   (custom) : {my_mode(data1)}")
print(f"Mode   (stdlib) : {statistics.mode(data1)}")
print(f"Mode   (scipy)  : {stats.mode(data1, keepdims=True).mode[0]}")


# ===========================================================
# EXAMPLE 2: Even-length dataset (tests median averaging)
# ===========================================================
data2 = [4, 8, 15, 16, 23, 42]

print("\n" + "=" * 60)
print("Example 2: Even-length dataset")
print("=" * 60)
print(f"Data: {data2}")
print(f"Mean   (custom) : {my_mean(data2):.4f}")
print(f"Median (custom) : {my_median(data2)}  (average of two middle values)")
print(f"Mode   (custom) : {my_mode(data2)}  (all unique -> every value is a mode)")


# ===========================================================
# EXAMPLE 3: Multimodal dataset (more than one mode)
# ===========================================================
data3 = [1, 2, 2, 3, 3, 4]

print("\n" + "=" * 60)
print("Example 3: Multimodal dataset")
print("=" * 60)
print(f"Data: {data3}")
print(f"Mode (custom) : {my_mode(data3)}  <- two values tied for most frequent")

try:
    print(f"Mode (stdlib) : {statistics.mode(data3)}  (picks first encountered on ties)")
except statistics.StatisticsError as e:
    print(f"Mode (stdlib) : Error - {e}")


# ===========================================================
# EXAMPLE 4: Real-world style data - exam scores
# ===========================================================
scores = [55, 62, 70, 70, 72, 75, 78, 80, 82, 85, 88, 90, 95]

print("\n" + "=" * 60)
print("Example 4: Exam scores summary")
print("=" * 60)
print(f"Scores: {scores}")
print(f"Mean   : {my_mean(scores):.2f}")
print(f"Median : {my_median(scores)}")
print(f"Mode   : {my_mode(scores)}")
print(f"\nInterpretation:")
print(f"  Mean ({my_mean(scores):.2f}) and median ({my_median(scores)}) are close,")
print(f"  suggesting the scores are fairly symmetric with no major outliers pulling")
print(f"  the mean up or down.")