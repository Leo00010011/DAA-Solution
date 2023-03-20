import optimal_solver, slow_solver, random_generator


def tester(cases_count :int, str_lenght :int):
    for i in range(cases_count):
        S, T = random_generator(str_lenght)
        real_value = slow_solver(S, T, True)
        actual_value = optimal_solver(S, T)
        
        with open("tests.txt", "w") as f:
            f.write(f"S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}\n")

        assert real_value == actual_value, f"Error: S = {S}, T = {T}, Real Value = {real_value}, Actual Value = {actual_value}"
    print("Todos los tests pasaron exitosamente.")