
def bubble_sort():
    numbers = [6, 2, 9, 1, 4]

    print("Before sorting:", numbers)

    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap the numbers
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("After sorting: ", numbers)


if __name__ == "__main__":
    bubble_sort()