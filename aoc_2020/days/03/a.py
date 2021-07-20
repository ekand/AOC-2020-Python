def main():
    forest = get_puzzle_input()
    x = 0
    y = 0
    forest_width = len(forest[0])
    forest_height = len(forest)
    dx = 3
    dy = 1
    trees_hit = 0
    while y < forest_height:
        if forest[y][x] == '#':
            trees_hit += 1
        x += dx
        y += dy
        x = x % forest_width
    print(trees_hit)  # 173


def get_puzzle_input():
    with open('input.txt') as f:
        lines = f.read().strip().split('\n')
    forest = [list(line) for line in lines]
    return forest


if __name__ == "__main__":
    main()
