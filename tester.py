from optimal_solver import optimal_solver
from slow_solver import slow_solver
from random_generator import random_generator 
from colorama import Fore, Back, Style
from random import randint
import pickle

def gen_cases(count,s_len = None, t_len = None):
    current_s_len = s_len
    current_t_len = t_len
    to_save = []
    for _ in range(count):
        if s_len == None:
            current_s_len = randint(1,200)
        if t_len == None:
            current_t_len = randint(1,current_s_len)
        S,T = random_generator(current_s_len,current_t_len)
        result = slow_solver(S,T,False)
        to_save.append({'s': S, 't' : T, 'result': result})
        if(count % 10 == 0):
            print(f'{count} cases saved >>>>')
            with open('test.txt', 'w') as file:
                pickle.dump(to_save,file)


def tester(cases_count :int, str_lenght :int):
    for i in range(cases_count):
        S, T = random_generator(str_lenght)
        print(f'Caso S = {S} y T = {T}')
        actual_value = optimal_solver(S, T)
        print(f'actual value = {actual_value}')
        real_value = slow_solver(S, T, False)
        print(f'real_value = {real_value}')
        
        with open("tests.txt", "w") as f:
            f.write(f"S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}\n")

        if real_value != actual_value:
            print(Fore.RED + f"Error: S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}")
            print(Fore.WHITE)
        else:
            print(Fore.GREEN + f"S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}\n")
            print(Fore.WHITE)

# S = 'nnavtvyfqheibwxbpunw'
# T = 'newvtpwn'

# print(optimal_solver(S,T))


# tester(100,20)

# gen_cases(1000)

list = [{'s':'abcd', 't':'cd', 'result': 1},{'s':'dcba', 't':'sd', 'result':45},{'s':'qwer', 't':'qw', 'result':48}]
with open('test.txt','w') as f:
    pickle.dump({'s':'abcd', 't':'cd', 'result': 1},f, protocol=-1)
