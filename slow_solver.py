def is_arr_prefix(arr,t):
    if(len(arr) <= len(t)):
        return False
    for i in range(len(t)):
        if(arr[i] != t[i]):
            return False
    return True


def slow_solver(s,t,print_sol):
    # print("Soluciones del problema para")
    # print('s: ' + s)
    # print('t: ' + t)
    return 2 * slow_solver_aux(s,t,[s[0]],[0],1, print_sol)

def slow_solver_aux(s,t,current_sol : list,choices,index,print_sol):    
    count = 0
    if is_arr_prefix(current_sol,t):
        if print_sol:
            print(''.join(current_sol) + ':' + str(choices))
        count = 1

    if(index == len(s)):
        return count

    current_sol.insert(0,s[index])
    choices.append(0)
    result_left =  slow_solver_aux(s,t,current_sol,choices,index + 1,print_sol)
    current_sol.pop(0)
    choices.pop()

    current_sol.append(s[index])
    choices.append(1)
    result_right = slow_solver_aux(s,t,current_sol,choices,index + 1,print_sol)
    current_sol.pop()
    choices.pop()

    return count + result_left + result_right
