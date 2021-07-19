def solve():
    with open('input.txt') as f:
        puzzle_input = f.read()

    nums = [int(s) for s in puzzle_input.strip().split('\n')]

    for i, num1 in enumerate(nums):
        for num2 in nums[i+1:]:
            total = num1 + num2
            if total == 2020:
                return num1 * num2


print(solve())  # 1018336
