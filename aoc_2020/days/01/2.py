def solve():
    with open('input.txt') as f:
        puzzle_input = f.read()

    nums = [int(s) for s in puzzle_input.strip().split('\n')]

    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            for num3 in nums[j+1:]:
                total = num1 + num2 + num3
                if total == 2020:
                    return num1 * num2 * num3


print(solve())  # 288756720
