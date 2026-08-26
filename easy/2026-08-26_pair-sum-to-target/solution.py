def pair_sum_to_target(array, target):
    seen = set()

    for num in array:
        complement = target - num

        if complement in seen:
            return True

        seen.add(num)

    return False


# Primer
array = [2, 7, 11, 15]
target = 9

print(pair_sum_to_target(array, target))  # True