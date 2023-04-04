def is_arr_prefix(arr,t):
    if(len(arr) < len(t)):
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

print(is_arr_prefix(['n'],'n'))
#Ejemplo 1:
#Soluciones del problema para
#s: abdbaedadb
#t: abda      
#abdab:[0, 1, 0, 0, 0]
#abdabe:[0, 1, 0, 0, 0, 1]
#abdabed:[0, 1, 0, 0, 0, 1, 1]
#abdabeda:[0, 1, 0, 0, 0, 1, 1, 1]
#abdabedad:[0, 1, 0, 0, 0, 1, 1, 1, 1]
#abdabedadb:[0, 1, 0, 0, 0, 1, 1, 1, 1, 1]
#abdabaed:[0, 1, 0, 0, 1, 1, 1, 0]
#abdabaedd:[0, 1, 0, 0, 1, 1, 1, 0, 1]
#abdabaeddb:[0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
#18

#Ejemplo 2:
#Soluciones del problema para
#s: abracadabra
#t: abra
#abrabacadar:[0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0]
#abrac:[0, 1, 1, 1, 1]
#abraca:[0, 1, 1, 1, 1, 1]
#abracad:[0, 1, 1, 1, 1, 1, 1]
#abracada:[0, 1, 1, 1, 1, 1, 1, 1]
#abracadab:[0, 1, 1, 1, 1, 1, 1, 1, 1]
#abracadabr:[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#abracadabra:[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#16


print(slow_solver('abdbaedadb','abda',True))
