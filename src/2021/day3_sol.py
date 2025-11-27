with open("day3_input") as f:
    data = f.read().splitlines()

full_data = "".join(data)
bin_nrs = len(data)
bit_length = len(data[0])

most_common_bits = ["1" if full_data[i::bit_length].count("1") >= bin_nrs / 2 else "0" for i in range(bit_length)]

gamma = int("".join(most_common_bits), 2)
epsilon = int("".join(["1" if x == "0" else "0" for x in most_common_bits]), 2)
print(f"Part1: {gamma * epsilon}")

oxygen = [x for x in data]
co2 = [x for x in data]




def get_rating(bin_list, isMost):
    new_list = [x for x in bin_list]

    for bit_index in range(len(bin_list[0])):
        loop_list = [x for x in new_list]

        digits_for_index = [bit[bit_index] for bit in loop_list]
        count_1 = digits_for_index.count("1")

        if isMost:
            if count_1 >= len(loop_list)/2:
                new_list = list(filter(lambda x: x[bit_index] == "1", loop_list))
            else:
                new_list = list(filter(lambda x: x[bit_index] == "0", loop_list))
        else:
            if count_1 >= len(loop_list)/2:
                new_list = list(filter(lambda x: x[bit_index] == "0", loop_list))
            else:
                new_list = list(filter(lambda x: x[bit_index] == "1", loop_list))

        if len(new_list) == 1:
            return int(new_list[0], 2)


ans = get_rating(oxygen, 1) * get_rating(co2, 0)

print(f"Part2: {ans}")
