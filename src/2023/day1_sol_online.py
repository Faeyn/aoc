numbers = {
    'zero': 'z0o',
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
}


def convert_words_to_digit(line):
    for key, value in numbers.items():
        line = line.replace(key, value)
    return line


with open('day1_input', 'r') as f:
    ans = 0
    for line in f:
        line = line.strip()
        og_line = line
        line = convert_words_to_digit(line)

        left = 0
        right = len(line) - 1
        while not line[left].isdigit():
            left += 1
        while not line[right].isdigit():
            right -= 1

        num = int(line[left]) * 10 + int(line[right])
        print(og_line, line, num)
        ans += num

    print(ans)