
lines_split = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        lines_split.append(line.split())

def check_seq(vector):
    distances = [int(vector[i]) - int(vector[i - 1]) for i in range(1, len(vector))]
    if all(d > 0 for d in distances) or all(d < 0 for d in distances):
        if all(-3 <= d <= 3 for d in distances):
            return True
    else:
        return False        

def part_1(input_data):
    sum_count = 0
    for i in input_data:
        if check_seq(i):
            sum_count += 1

    return sum_count

def part_2(input_data):
    sum_count = 0
    def check_seq_2(vector):
        if check_seq(vector):
            return True

        for i in range(len(vector)): 
            new_vector = vector[:i] + vector[i+1:]
            if check_seq(new_vector):
                return True
        return False

    for i in input_data:
        if check_seq_2(i):
            sum_count += 1

    return sum_count

print("Part 1:", part_1(lines_split))
print("Part 2:", part_2(lines_split))