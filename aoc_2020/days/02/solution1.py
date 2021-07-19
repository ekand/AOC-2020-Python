from collections import Counter


def main():
    lines = get_input()
    valid_lines = 0
    for line in lines:
        if validate(*parse(line)):
            valid_lines += 1
    print(valid_lines)  # 564


def validate(min_count, max_count, restricted_letter, password):
    password_counter = Counter(password)
    return (min_count <=
            password_counter[restricted_letter] <= max_count)


def parse(line):
    counts, letter, password = line.split(" ")
    min_count, max_count = [int(s) for s in counts.split("-")]
    restricted_letter = letter[0:1]
    # password = password
    return min_count, max_count, restricted_letter, password


def get_input():
    with open('input.txt') as f:
        raw_input = f.read()
    lines = raw_input.strip().split("\n")
    return lines


if __name__ == "__main__":
    main()
