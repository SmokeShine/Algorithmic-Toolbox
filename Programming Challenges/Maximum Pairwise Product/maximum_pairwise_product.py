# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    max_value=0
    max_index=0
    second_max_value=0
    second_max_index=0
    # max
    for i in range(len(numbers)):
        if numbers[i]>max_value:
            max_value=numbers[i]
            max_index=i
    # max_value max
    for i in range(len(numbers)):
        if (numbers[i]>=second_max_value) and (max_index!=i):
            second_max_value=numbers[i]
            second_max_index=i
    return max_value*second_max_value
if __name__ == '__main__':
    n = int(input())

    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))

