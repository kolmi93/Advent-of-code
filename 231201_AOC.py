# https://adventofcode.com/2023/day/1#part2

# ÚKOL Č. 1:
import re

all = []
with open('231201_AOC_data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        numbers = re.findall(r'\d+',line)
#        numbers = re.sub(r'[a-zA-Z]', '', line)
        if numbers:
            first = numbers[0][0]
            last = numbers[-1][-1]
            new_number = first+last
            all.append(int(new_number))
        else:
            continue
print(sum(all))

# ÚKOL Č.2:
