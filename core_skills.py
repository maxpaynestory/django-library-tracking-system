import random


def filter_method(number):
    if number < 10:
        return True
    else:
        return False


list_of_numbers = range(1, 20)
rand_list = random.sample(list_of_numbers, 10)

list_comprehension_below_10 = [item for item in rand_list if item < 10]

list_comprehension_below_10 = rand_list.filter(filter_method)