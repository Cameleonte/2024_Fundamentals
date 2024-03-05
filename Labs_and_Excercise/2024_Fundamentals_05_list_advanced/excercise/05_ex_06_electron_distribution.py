def main_atom(used_electrons):
    list_shell_done = []
    shell = 1

    while used_electrons > 0:
        max_electrons = 2 * shell ** 2
        if max_electrons >= used_electrons:
            list_shell_done.append(used_electrons)
            used_electrons -= max_electrons
        else:
            list_shell_done.append(max_electrons)
            used_electrons -= max_electrons
        shell += 1
    return list_shell_done


given_number = int(input())
result = main_atom(given_number)
print(result)
