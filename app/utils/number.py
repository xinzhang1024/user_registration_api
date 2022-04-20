
import random


def get_4_digits():
    res = ''
    for i in range(4):
        res += str(random.randint(0, 9))

    return res
