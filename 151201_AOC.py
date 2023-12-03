# https://adventofcode.com/2015/day/1#part2

list = []
floor = 0
with open('150112_AOC_data.txt', 'r') as file:
    for line in file:
        print(line.strip())
floor = 0
floor_2 = 0
for character in line:
    if character == '(())' or character == '()()':
        floor = 0
        floor_2 = 0
        list.append(floor_2)
    elif character ==  '(((' or character == '(()(()(' or character == '))(((((':
        floor = 3
        floor_2 += 3
        list.append(floor_2)
    elif character == '())' or character == '))(':
        floor = -1
        floor_2 = -1
        list.append(floor_2)
    elif character == ')))' or character == ')())())':
        floor = -3
        floor_2 = -3
        list.append(floor_2)
    elif character == '(':
        floor += 1
        floor_2 += 1
        list.append(floor_2)
    else:
        floor -= 1
        floor_2 -= 1
        list.append(floor_2)
print(floor)
print(list.index(-1)+1)