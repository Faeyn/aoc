from advent_code.aoc_utils import get_nums

with open('day17input') as f:
    data = f.read().splitlines()

prog = get_nums(data[4])


def get_output(a_register):
    combo_operants = {
        0: 0, 1: 1, 2: 2, 3: 3,
        4: a_register,
        5: get_nums(data[1])[0],
        6: get_nums(data[2])[0],
        7: None
    }

    output = []

    def adv(l_operand):
        combo_operants[4] = int(combo_operants[4] / 2 ** combo_operants[l_operand])

    def bxl(l_operand):
        combo_operants[5] = int(combo_operants[5] ^ l_operand)

    def bst(l_operand):
        combo_operants[5] = int(combo_operants[l_operand] % 8)

    def jnz(l_operand):
        if combo_operants[4] == 0:
            return float('inf')

        return l_operand

    def bxc(l_operand):
        combo_operants[5] = int(combo_operants[5] ^ combo_operants[6])

    def out(l_operand):
        output.append(combo_operants[l_operand] % 8)

    def bdv(l_operand):
        combo_operants[5] = int(combo_operants[4] / 2 ** combo_operants[l_operand])

    def cdv(l_operand):
        combo_operants[6] = int(combo_operants[4] / 2 ** combo_operants[l_operand])

    ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    pointer = 0

    while pointer < len(prog):
        jump = ops[prog[pointer]](prog[pointer + 1])

        if jump is not None:
            pointer = jump
        else:
            pointer += 2

    return output


print('Ans1: ', ','.join(str(x) for x in get_output(get_nums(data[0])[0])))


def find_a(a_register, power, cs):
    for i in range(8):
        new_a = a_register + i * 8 ** power

        output = get_output(new_a)
        if output == prog:
            return new_a

        if output[power] == prog[power]:
            a = find_a(new_a, power - 1, cs + [i])
            if a:
                return a


print('Ans2: ', find_a(8 ** 15, 14, [1]))
