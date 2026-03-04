import random

MAX_ATTEMPTS = 5
EXCLUDED_CHARS = ('ь', 'ъ', 'ы')

def load_cities(filename="cities.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        cities_list = [line.strip().lower() for line in f]
    return cities_list

def get_last_char(city):
    if city[-1] in EXCLUDED_CHARS:
        return city[-2]
    else:
        return city[-1]

def validate_user_city(user_city, current_city, cities_list, used_cities):
    if user_city in used_cities:
        return False, "Этот город уже был назван."
    if user_city not in cities_list:
        return False, "Такого города нет в списке."
    expected_char = get_last_char(current_city)
    if not user_city.startswith(expected_char):
        return False, f"Город должен начинаться на букву {expected_char.upper()}"
    return True, ""

def get_computer_city(last_char, cities_list, used_cities):
    for city in cities_list:
        if city.startswith(last_char) and city not in used_cities:
            return city
    return None

def game():
    cities_list = load_cities()
    used_cities = set()
    attempts = MAX_ATTEMPTS
    current_city = random.choice(cities_list)
    print("Ход компьютера:", current_city.capitalize())
    used_cities.add(current_city)

    while attempts > 0:
        user_city = input("Ваш ход: ").lower()
        is_valid, message = validate_user_city(user_city, current_city, cities_list, used_cities)

        if is_valid:
            used_cities.add(user_city)
            last_char = get_last_char(user_city)
            computer_city = get_computer_city(last_char, cities_list, used_cities)

            if computer_city:
                print("Ход компьютера:", computer_city.capitalize())
                used_cities.add(computer_city)
                current_city = computer_city
            else:
                print("Компьютер не смог найти город. Вы победили!")
                return
        else:
            attempts -= 1
            print(f"{message} Осталось попыток: {attempts}")
            if attempts == 0:
                print("У вас не осталось попыток. Вы проиграли!")
                return

if __name__ == "__main__":
    game()

