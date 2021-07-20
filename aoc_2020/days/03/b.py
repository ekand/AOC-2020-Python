def main():
    forest = get_puzzle_input()
    result = 1
    slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (dx, dy)
    for slope in slopes:
        dx, dy = slope
        trees = count_trees(forest, dx, dy)
        result *= trees
    print(result)  # 4385176320


def count_trees(forest, dx, dy):
    x = 0
    y = 0
    forest_width = len(forest[0])
    forest_height = len(forest)

    trees_hit = 0
    while y < forest_height:
        if forest[y][x] == '#':
            trees_hit += 1
        x += dx
        y += dy
        x = x % forest_width
    return trees_hit


def get_puzzle_input():
    with open('input.txt') as f:
        lines = f.read().strip().split('\n')
    forest = [list(line) for line in lines]
    return forest


if __name__ == "__main__":
    main()
