import random
import string

def random_generator( n: int):
    # Generar cadena aleatoria de longitud n
    S = ''.join(random.choices(string.ascii_lowercase, k=n))

    # Crear una cadena aleatoria T a partir de un subconjunto de caracteres de S
    T_len = random.randint(1, n)
    T_chars = random.sample(S, T_len)
    T = ''.join(T_chars)

    return S, T

