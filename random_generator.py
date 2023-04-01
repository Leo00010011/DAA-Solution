import random as rd
import string


def random_generator(s_len = None, t_len = None):
    if s_len is None:
        s_len = rd.randint(1,200)
    if t_len is None:
        t_len = rd.randint(1,s_len)
        
    S = ''.join(rd.choices(string.ascii_lowercase, k = s_len))
    T = ''.join(rd.sample(S, k = t_len))

    return S, T




# S, T = random_generator(10)
# print("S =", S)
# print("T =", T)
