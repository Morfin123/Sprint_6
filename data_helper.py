import random


class OrderPageDataHelper:
    def get_random_time_rental():
        choice = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']
        random_index = random.randrange(len(choice))
        time_rental = choice[random_index]
        return time_rental

    def get_random_colour():
        choice = ['black', 'grey']
        random_index = random.randrange(len(choice))
        colour = choice[random_index]
        return colour

    def get_random_phone():
        phone = f'79{random.randint(100000000, 999999999)}'
        return phone

    def get_random_metro():
        return random.randint(1, 237)