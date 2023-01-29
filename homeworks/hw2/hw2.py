from typing import Dict


def read_file(file: str):
    """
    Dosyayı okuyup içindeki değerleri dictionary ile dönme.
    :param file: file name
    :return: Dict[isim:yer]
    """
    d = {}
    with open(f"{file}.txt") as f:
        for line in f:
            split_line = line.split()
            key = split_line[0]
            val = split_line[1]
            d[key] = val

    return d


def find_and_update_value(values: dict, target: str):
    """
    Hedef kelimeyi verinin içinden arıyor. Hedef varsa print edilir. Yoksa kullanıcıdan değeri alınır ve dict e atılır.
    :param values:
    :param target:
    :return:
    """
    if target in values:
        print(f'{target} was born in {values[target]}')
    else:
        place = input(f"Tell me a place for user {target}")
        values[target] = place
        print(f'Saved.')


def main():
    file = 'hw2'
    my_dict = read_file(file)

    while True:
        name = input('Name: ')
        if name == "exit":
            return
        find_and_update_value(my_dict, name)


main()
