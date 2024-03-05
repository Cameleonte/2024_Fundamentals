def calculate_bmi(value_weight, value_height):
    """Calculate the Body Mass Index (BMI)."""
    value_bmi = value_weight / value_height ** 2
    return value_bmi


def calculate_calories_burned(exercise_duration):
    """Calculate the estimated number of calories burned during exercise.
    People can expect to burn 8–15 calories per minute if doing high intensity interval training.
    We assume an average value of 11,5 calories per minute"""
    average_value_of_calories_burned_per_minute = 11.5
    value_calories_burned = exercise_duration * average_value_of_calories_burned_per_minute
    return value_calories_burned


def filter_overweight_people(people_data_list):
    """Filter overweight people based on BMI."""
    overweight_people_list = []
    for sportsman in people_data_list:
        value_bmi = calculate_bmi(sportsman['weight'], sportsman['height'])
        if value_bmi >= 25:
            overweight_people_list.append(sportsman)
    return overweight_people_list


# Main program
people_data = []

print("Enter fitness data for each person (Enter a blank name to finish):")
while True:
    name = input("Enter a person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter a person's weight in kilograms: "))
    height = float(input("Enter a person's height in meters: "))
    duration = float(input("Enter an exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

overweight_people = filter_overweight_people(people_data)
if overweight_people:
    print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")
else:
    print("\nNo overweight people")
