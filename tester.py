from optimal_solver import optimal_solver
from slow_solver import slow_solver
from random_generator import random_generator, random_right
from colorama import Fore, Back, Style
from random import randint
import json
import os.path

def gen_cases(count,rand_func = random_generator,s_len = None, t_len = None, file_path = 'test.txt' ):
    to_save = []
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path,'r') as fin:
            to_save = json.load(fin)
    for i in range(count):
        S,T = rand_func(s_len,t_len)
        print(f'>>>> case {i + 1}')
        print(f'S = {S}')
        print(f'T = {T}')
        result = slow_solver(S,T,False)
        print(f'result = {result}')
        to_save.append({'s': S, 't' : T, 'result': result})
        if(i % 10 == 0):
            print(f'{i + 1} cases saved >>>>')
            with open(file_path, 'w') as file:
                json.dump(to_save,file)
    with open(file_path, 'w') as file:
        json.dump(to_save,file)
        
def json_tester(file_path = 'test.txt'):
    to_save = []
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path,'r') as fin:
            to_save = json.load(fin)
    wrong_answer = []
    cant_solo_dcha = 0
    cant_solo_izda = 0
    cant_izda = 0
    cant_dcha = 0
    cant_izda_dcha = 0
    cant_zero = 0
    for case in to_save:
        S = case['s']
        T = case['t']
        # print(f'Caso S = {S} y T = {T}')
        real_value = case['result']
        if(real_value == 0):
            cant_zero += 1
        # print(f'real_value = {real_value}')
        actual_value, dcha, izda = optimal_solver(S, T)
        if(dcha):
            cant_dcha += 1
            if (not izda):
                cant_solo_dcha += 1
            else:
                cant_izda_dcha += 1
        if(izda):
            cant_izda += 1
            if (not dcha):
                cant_solo_izda += 1
        
        # print(f'actual value = {actual_value}')

        if real_value != actual_value:
            # print(Fore.RED + f"Error: S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}")
            # print(Fore.WHITE)
            wrong_answer.append({'s':S,'t':T,'actual':actual_value,'real':real_value,'dcha':dcha})
        # else:
            # print(Fore.GREEN + f"S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}\n")
            # print(Fore.WHITE)
    
    print('SUMARY:')
    print('wrong cases:')
    cant_wrong_right = 0
    for case in wrong_answer:
        S = case['s']
        T = case['t']
        actual_value = case['actual']
        real_value = case['real']
        dcha = case['dcha']
        if dcha:
            cant_wrong_right += 1
        print(Fore.RED + f"Error: S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}, dcha = {dcha}")
        print(Fore.WHITE)
    print(f'cant_wrong: {len(wrong_answer)}')
    print(f'cant_right: {cant_dcha}')
    print(f'cant_wrong_right: {cant_wrong_right}')
    print(f'cant_wrong_left: {len(wrong_answer) - cant_wrong_right}')

    print(f'accuracy: {(len(to_save) - len(wrong_answer))/len(to_save)}')
    print(f'right_rat: {cant_dcha/len(to_save)}')
    print(f'left_rat: {cant_izda/len(to_save)}')
    print(f'only_right_rat: {cant_solo_dcha/len(to_save)}')
    print(f'only_left_rat: {cant_solo_izda/len(to_save)}')
    print(f'left_and_right_rat: {cant_izda_dcha/len(to_save)}')
    print(f'zero_rat: {cant_zero/len(to_save)}')

    print(f'right_accuracy: {(cant_dcha - cant_wrong_right)/cant_dcha}')

        
    


def tester(cases_count :int, str_lenght :int):
    wrong_answer = []
    cant_dcha = 0
    for i in range(cases_count):
        S, T = random_generator(str_lenght)
        print(f'Caso S = {S} y T = {T}')
        actual_value, dcha = optimal_solver(S, T)
        if(dcha):
            cant_dcha += 1
        print(f'actual value = {actual_value}')
        real_value = slow_solver(S, T, False)
        print(f'real_value = {real_value}')
        
        with open("tests.txt", "w") as f:
            f.write(f"S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}\n")

        if real_value != actual_value:
            print(Fore.RED + f"Error: S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}")
            print(Fore.WHITE)
            wrong_answer.append({'s':S,'t':T,'actual':actual_value,'real':real_value,'dcha':dcha})
        else:
            print(Fore.GREEN + f"S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}\n")
            print(Fore.WHITE)

    print('SUMARY:')
    print('wrong cases:')
    for case in wrong_answer:
        S = case['s']
        T = case['t']
        actual_value = case['actual']
        real_value = case['real']
        dcha = case['dcha']
        print(Fore.RED + f"Error: S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}, dcha = {dcha}")
        print(Fore.WHITE)
    print(f'accuracy: {len(wrong_answer)/cases_count}')
    print(f'right_rat: {dcha}')






