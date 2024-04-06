def find_insert_position(array: list[int], x: int) -> int:
    for i in range(len(array)):
        if x <= array[i]:
            return i
    return len(array)


if __name__ == '__main__':
    array = [1, 2, 3, 3, 3, 5]
    n = 4
    assert find_insert_position(array, n) == 5
    array.insert(5, n)
    assert array == sorted(array)