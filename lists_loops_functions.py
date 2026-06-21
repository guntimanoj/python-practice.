def sum_list(numbers):
    """Return the sum of a list of numbers using a loop (not sum())."""
    total = 0
    for n in numbers:
        total += n
    return total


def find_max(numbers):
    """Return the largest value in a list using a loop."""
    if not numbers:
        raise ValueError("find_max() called on empty list")
    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest


def filter_even(numbers):
    """Return only the even numbers from a list."""
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens


def reverse_list(items):
    """Return a reversed copy of a list without using items[::-1]."""
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item)
    return reversed_items


def count_occurrences(items, target):
    """Count how many times target appears in items."""
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count


if __name__ == "__main__":
    data = [4, 2, 9, 1, 7, 2, 5]

    print("List:", data)
    print("Sum:", sum_list(data))
    print("Max:", find_max(data))
    print("Evens:", filter_even(data))
    print("Reversed:", reverse_list(data))
    print("Occurrences of 2:", count_occurrences(data, 2))