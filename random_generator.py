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
    if t_len is None:
        t_len = rd.randint(2,15)
    t = rd.choices(string.ascii_lowercase,k = t_len)
    T = ''.join(t)
    suffix_index = rd.randint(0,len(t) - 2)
    t_suffix = t[suffix_index: - 1]
    t_middle = t[:suffix_index]
    rd.shuffle(t_suffix)
    s_prefix = ''.join(t_suffix + [T[-1]])

    if s_len is None:
        s_len = rd.randint(t_len,25)
    
    s_suffix = rd.choices(string.ascii_lowercase,k = s_len - t_len) + t_middle
    rd.shuffle(s_suffix)
    s_suffix = ''.join(s_suffix)
    S = s_prefix + s_suffix
    return S,T



