import re


def validate_info(info):
    pattern = r'%([A-Z][a-z]+)%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|(\d+)\|[^\|\$\%\.\d]*(\d+\.*\d+)\$'
    current_list = re.findall(pattern, info)
    if current_list:
        return True, current_list


def main_operations(current_info):
    all_products_price = 0
    while current_info != 'end of shift':
        tot_product_prince = 0
        if validate_info(current_info):
            new_list = validate_info(current_info)[1]
            customer, product, count, price = list(i for i in new_list[0])
            tot_product_prince = int(count) * float(price)
            all_products_price += tot_product_prince
            print(f"{customer}: {product} - {tot_product_prince:.2f}")
        current_info = input()
    return all_products_price


current_order_info = input()

tot_price = main_operations(current_order_info)
print(f'Total income: {tot_price:.2f}')
