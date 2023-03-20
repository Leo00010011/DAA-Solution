import random as rd
import string


def random_generator(n : int):
    S = ''.join(rd.choices(string.ascii_lowercase, k = n))

    T_len = rd.randint(1, n)
    T_chars = rd.sample(S, k = T_len)
    T = ''.join(T_chars)

    return S, T


S, T = random_generator(10)
print("S =", S)
print("T =", T)
