import random as rd
import string


def random_generator(s_len = None, t_len = None):
    if s_len is None:
        s_len = rd.randint(1,25)
    if t_len is None:
        t_len = rd.randint(1,s_len)
        
    S = ''.join(rd.choices(string.ascii_lowercase, k = s_len))
    T = ''.join(rd.sample(S, k = t_len))

    return S, T


def random_right(s_len = None, t_len = None):
    if s_len is None:
        s_len = rd.randint(3,25)
    if t_len is None:
        t_len = rd.randint(2,s_len)
    right_len = rd.randint(1,len(t_len))

    s_prefix = rd.shuffle()


