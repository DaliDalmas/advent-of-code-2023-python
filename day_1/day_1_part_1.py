
# read lines from data
my_sum = 0

# part one
with open('./day_1/input.txt') as file:
    for line in file:
        line_split = [c for c in line if c.isdigit()]

        if len(line_split) == 1:
            my_sum += int(2*line_split[0])

        elif len(line_split)>1:
            my_sum += int(line_split[0]+line_split[-1])

print(my_sum)