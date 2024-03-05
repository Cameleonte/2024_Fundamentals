def calculate_happiness_values():
    employees_happiness = list(map(int, input().split()))
    improvement_factor = int(input())
    happiness_new_values = [a * improvement_factor for a in employees_happiness]
    average_happiness = sum(happiness_new_values) / len(happiness_new_values)
    happy_count = sum(y >= average_happiness for y in happiness_new_values)
    total_count = len(happiness_new_values)
    happy_or_not = 'happy' if happy_count >= total_count / 2 else 'not happy'

    result = f'Score: {happy_count}/{total_count}. Employees are {happy_or_not}!'

    return result


result = calculate_happiness_values()
print(result)
