# Maximum Consecutive Ones
def max_consecutive_ones(nums):
    longest = 0
    current = 0
    for n in nums:
        if n == 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 0          # prekid niza jedinica → resetuj brojač
    return longest


def solution():
    # Primeri
    print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))  # 3
    print(max_consecutive_ones([1, 0, 1, 1, 0, 1]))  # 2
    print(max_consecutive_ones([0, 0, 0]))           # 0
    print(max_consecutive_ones([1, 1, 1, 1]))        # 4


if __name__ == '__main__':
    solution()
