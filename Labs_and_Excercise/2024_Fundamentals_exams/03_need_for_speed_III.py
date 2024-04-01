def drive_cars(current_car, current_distance, current_fuel, initial_data, init_dict):
    init_miles = int(initial_data[0])
    init_fuel = int(initial_data[1])
    if int(current_fuel) > init_fuel:
        print('Not enough fuel to make that ride')
    else:
        init_miles += int(current_distance)
        init_fuel -= int(current_fuel)
        init_dict[current_car] = [init_miles, init_fuel]
        print(f'{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.')
        if int(init_miles) >= 100000:
            del init_dict[current_car]
            print(f'Time to sell the {current_car}!')


def refuel_cars(current_car, current_fuel, initial_data, init_dict):
    init_miles = int(initial_data[0])
    init_fuel = int(initial_data[1])
    refiled_tank = init_fuel + int(current_fuel)
    used_fuel = int(current_fuel)
    if refiled_tank > 75:
        refiled_tank = 75
        used_fuel = 75 - init_fuel
    init_dict[current_car] = [init_miles, refiled_tank]
    print(f'{current_car} refueled with {used_fuel} liters')


def revert_cars(current_car, reverted_distance, initial_data, init_dict):
    old_mileage = int(initial_data[0])
    init_fuel = int(initial_data[1])
    new_mileage = int(old_mileage) - int(reverted_distance)
    if new_mileage < 10000:
        new_mileage = 10000
    init_dict[current_car] = [new_mileage, init_fuel]
    print(f'{current_car} mileage decreased by {reverted_distance} kilometers')


def final_print(final_dictionary):
    for car in final_dictionary.keys():
        mileage = final_dictionary[car][0]
        fuel = final_dictionary[car][1]
        print(f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')


def main_function():
    initial_dictionary = {}

    for car_num in range(1, cars_number + 1):
        cars_information = input()
        car_brand, init_mileage, init_fuel = cars_information.split('|')
        initial_dictionary[car_brand] = [init_mileage, init_fuel]

    command = input()
    while command != 'Stop':
        action = command.split(' : ')[0]
        if action == 'Drive':
            action, car_model, distance, fuel = command.split(' : ')
            drive_cars(car_model, distance, fuel, initial_dictionary[car_model], initial_dictionary)
        elif action == 'Refuel':
            action, car_model, fuel = command.split(' : ')
            refuel_cars(car_model, fuel, initial_dictionary[car_model], initial_dictionary)
        elif action == 'Revert':
            action, car_model, distance = command.split(' : ')
            revert_cars(car_model, distance, initial_dictionary[car_model], initial_dictionary)
        command = input()
    final_print(initial_dictionary)


cars_number = int(input())
main_function()
