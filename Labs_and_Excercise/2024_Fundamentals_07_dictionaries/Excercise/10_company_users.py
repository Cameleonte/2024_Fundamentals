def adding_function():
    if company_title not in company_dictionary:
        company_dictionary[company_title] = [employee_id]
    else:
        if len(company_dictionary[company_title]) >= 1 and employee_id not in company_dictionary[company_title]:
            company_dictionary[company_title] += [employee_id]


company_dictionary = {}

while True:
    company_info = input()
    if company_info == 'End':
        break
    company_title, employee_id = company_info.split(' -> ')
    adding_function()

for comp_name, id_employee_list in company_dictionary.items():
    print(f'{comp_name}')
    for id in id_employee_list:
        print(f'-- {id}')
