from optimal_solver import optimal_solver
from slow_solver import slow_solver
from random_generator import random_generator 
from colorama import Fore, Back, Style
from random import randint
import json
import os.path

def gen_cases(count,s_len = None, t_len = None):
    to_save = []
    if os.path.exists('test.txt') and os.path.isfile('tests.txt'):
        with open('test.txt','r') as fin:
            to_save = json.load(fin)
    for i in range(count):
        S,T = random_generator(s_len,t_len)
        print(f'>>>> case {i + 1}')
        print(f'S = {S}')
        print(f'T = {T}')
        result = slow_solver(S,T,False)
        print(f'result = {result}')
        to_save.append({'s': S, 't' : T, 'result': result})
        if(i % 10 == 0):
            print(f'{i + 1} cases saved >>>>')
            with open('test.txt', 'w') as file:
                json.dump(to_save,file)

def json_tester(file_path = 'test.txt'):
    to_save = []
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path,'r') as fin:
            to_save = json.load(fin)
    
    for case in to_save:
        S = case['s']
        T = case['t']
        print(f'Caso S = {S} y T = {T}')
        real_value = case['result']
        print(f'real_value = {real_value}')
        actual_value = optimal_solver(S, T)
        print(f'actual value = {actual_value}')

        if real_value != actual_value:
            print(Fore.RED + f"Error: S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}")
            print(Fore.WHITE)
        else:
            print(Fore.GREEN + f"S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}\n")
            print(Fore.WHITE)
        
    


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

S = 'eoof'
T = 'oeof'
print(slow_solver(S,T,False))
print(optimal_solver(S,T))
# tester(100,20)
# temp = [{'s': 'Pepe','number': 15 },{'s': 'Maria','number': 55 },{'s': 'Leo','number': 200}]

# with open('tests.txt','w') as fout:
#     json.dump(temp,fout)


json_tester()

# gen_cases(1000)


