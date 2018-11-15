from random import randint
from itertools import groupby
a = [random.randint(0,9) for _ in range(2500)]
max((list(g) for k, g in groupby(a)), key=len)