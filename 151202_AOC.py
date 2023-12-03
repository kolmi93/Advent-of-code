# https://adventofcode.com/2015/day/2

data = open('151202_AOC_data.txt').read().splitlines()
data = [d.split('x') for d in data]
data = [list(map(int, d)) for d in data]

paper = 0
ribbon = 0
for one in data:
    a = (one[0] * one[1])
    b = (one[1] * one[2])
    c = (one[2] * one[0])
    all = [a,b,c]
    paper += 2*a + 2*b + 2*c + min(all)

    total = [one[0], one[1], one[2]]
    ribbon += (2*(one[0]) + 2*(one[1]) + 2*(one[2])) - 2*max(total) + (one[0]*one[1]*one[2])

print(paper)
print(ribbon)