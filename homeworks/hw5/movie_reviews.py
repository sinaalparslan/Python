from user import User
from movie import Movie

def read_file(file: str):
    """
    Dosyayı okuyup içindeki değerleri dictionary ile dönme.
    :param file: file name
    :return:
    """
    d = {}
    movie_genre=()
    with open(f"{file}") as f:
        for line in f:
            split_line = line.split("|")
            movie_number = split_line[0]
            movie_name = split_line[1]
            movie_time = split_line[2]
            movie_link = split_line[3]
            movie_genre =split_line[4-22]
            d.setdefault(f'{movie_number}', []).append(f'{movie_name}')
            d.setdefault(f'{movie_number}', []).append(f'{movie_time}')
            d.setdefault(f'{movie_number}', []).append(f'{movie_link}')
            d.setdefault(f'{movie_number}', []).append(f'{movie_genre}')

    return d

def main():
     a = read_file("u.item")
     print(a)

main()