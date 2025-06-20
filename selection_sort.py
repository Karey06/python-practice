def selection_sort():
    numbers = [12, 4, 7, 3, 10, 1]

    print("Before sorting:", numbers)

    for i in range(len(numbers)):

        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    print("After sorting: ", numbers)


if __name__ == "__main__":
    selection_sort()

