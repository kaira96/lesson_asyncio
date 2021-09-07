<<<<<<< HEAD
from time import time
=======
# 1 Терминал python3 original.py
# 2 Терминал nc localhost:5001
# 3 Терминал nc localhost:5001

import socket
import selectors
>>>>>>> 5f9497762a7c49101470cb47f95d767c64f332b6

# python3 -i original.py
# gen
# g
# next(g)


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)

        yield pattern.format(str(t))

        sum = 234 + 234
        print(sum)


# g = gen_filename()


def gen1(s):
    for i in s:
        yield i



def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('oleg')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
