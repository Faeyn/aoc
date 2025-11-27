import re

with open('day3_input') as f:
    data = f.read().replace('\n', '')


def get_ans(matches):
    ans = 0
    for match in matches:
        x, y = re.findall('\d+', match)
        ans += int(x) * int(y)
    return ans


pattern = 'mul\(\d+,\d+\)'

alt_data = re.sub("don't\(\).*?do\(\)", '', data)
alt_data = re.sub("don't\(\).+", '', alt_data)

print('ans1', get_ans( re.findall(pattern, data)), 'ans2', get_ans(re.findall(pattern, alt_data)))