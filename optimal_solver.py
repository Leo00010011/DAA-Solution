
# def left_sol(S,T):
#     S_t = S[::-1]
#     solution = [[0 for j in range(len(T))] for j in range(len(S))]

#     for i in range(len(S)):
#         for j in range(len(T)):
#             solution[i][j] = solution[i - 1][j]
#             if S_t[i] == T[j] and j<= i:
#                 if j - 1 >= 0: # no es la columna 0
#                     solution[i][j] += solution[i-1][j-1]
#                 else:
#                     solution[i][j] += i + 1 # nada mas se cumple en la 1ra letra de de la cadena T
#                 if j == len(T) - 1:
#                     solution[i][j] += - solution[i-1][j-1] + 2^(len(S) - i + 1)*solution[i-1][j-1]
#     return solution[len(S) - 1][len(T) - 1],solution

def left_sol(S,T):
    if len(T) == 1:
        result = 0
        for i in range(len(S)):
            if S[i] == T[0]:
                result += (2**i)*(len(S) - i)
        return result, None

    result = [[0]*len(T)]
    for i in range(len(S) - 1, -1,-1):
        result.insert(0,[])
        for j in range(len(T)):
            if T[j] != S[i]:
                result[0].append(result[1][j])
            else:
                if j == 0:
                    result[0].append(result[1][j] + (len(S) - i))
                elif j == (len(T) - 1):
                    result[0].append(result[1][j] + result[1][j - 1] * (2**i))
                else:
                    result[0].append(result[1][j] + result[1][j - 1])
    result.pop(len(S))
    return result[0][len(T) - 1], result



def right_sol(S,T, left_dp):
    if len(T) == 1:
        if T[0] == S[0]:
            return len(S)
        else:
            return 0

    # buscar la ultima derecha valida de los primeros T
    m = -1
    for i in range(len(T) - 1, -1 , -1):
        if S[i] == T[len(T) - 1]:
            m = i
            break
    
    if m == -1:
        return 0
    
        
    # construir right_dp
    #   construir el caso de tamaño uno
    right_dp = [[]]
    for i in range(m):
        if S[0] == T[((len(T) - 1) - m) + i]:
            right_dp[0].append(2)
        else:
            right_dp[0].append(0)
    #   construir el resto de casos
    for l in range(2,m + 1):
        right_dp.append([])
        for pos in range(m - (l - 1)):
            current = 0
            if S[l - 1] == T[((len(T) - 1) - m) + pos]:
                current += right_dp[l -2][pos + 1]
            if S[l - 1] == T[((len(T) - 1) - m) + (pos + (l - 1))]:
                current += right_dp[l - 2][pos]
            right_dp[l - 1].append(current)
    #acumular las soluciones
    result = 0
    for i in range(m,-1,-1):
        if S[i] == T[len(T) - 1]:
            if i == 0:
                result += left_dp[1][len(T) - 2]
            elif i == (len(T) - 1):
                result += right_dp[i - 1][m - i]*(len(S) - len(T) + 1)
            else:
                result += left_dp[i + 1][len(T) - i - 2]*right_dp[i - 1][m - i]
    return result


def optimal_solver(S, T) -> int:
    result, left_dp = left_sol(S,T)
    right = right_sol(S,T,left_dp)
    return result + right, right > 0, result > 0


