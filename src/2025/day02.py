f = open('.input/day02_input')
data = f.read()
f.close()

# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def repeating_nr(nr: str) -> bool:
    i = len(nr)
    return nr[:int(i/2)] == nr[int(i/2):] 

def m_repeating_nr(nr: str) -> bool:
    l = len(nr)
    for i in range(1, int(l / 2)+1):
        if nr[:i] * int(l/i) == nr:
            return True
    return False
        
part_1 = 0
part_2 = 0
for r in data.split(","):
    start, end = r.split("-")
    for id in range(int(start), int(end) + 1):
        if repeating_nr(str(id)):
            part_1 += id

        if m_repeating_nr(str(id)):
            part_2 += id

print("Part1: ", part_1)
print("Part2: ", part_2)
        

