from user import User
from movie import Movie
import generalcode
import os
import glob
import re


def movie_parsing():
    moveis = []
    movie_data = generalcode.read_file('u.item')
    for count, element in enumerate(movie_data):
        moveis.append(Movie(element[0], element[1], element[2], element[3], element[4:23]))

    return moveis


def user_parsing():
    users = []
    user_data = generalcode.read_file('u.user')
    for count, element in enumerate(user_data):
        users.append(User(element[0], element[1], element[2], element[3], element[4]))

    return users


def genre_parsing():
    genres = {}
    with open("u.genre") as genre_data:
        for element in genre_data:
            split_line = element.replace("\n", "").split("|")
            key = split_line[1]
            val = split_line[0]
            genres[key] = val

    return genres


def occupation_parsing():
    occupation = {}
    with open("u.occupation") as occupation_data:
        for element in occupation_data:
            split_line = element.replace("\n", "").split("|")
            key = split_line[0]
            val = split_line[1]
            occupation[key] = val

    return occupation


def stage_1_step_1():
    moveis = movie_parsing()
    genres = genre_parsing()
    users = user_parsing()
    occupation = occupation_parsing()
    for element in range(len(moveis)):
        for count, genre in enumerate(moveis[element].genre_binary):
            if genre == '1':
                moveis[element].genre_human_readable.append(genres[f"{count}"])

        # print(moveis[element].movie_genre)
    for user in users:
        for index in range(1, len(occupation)):
            if user.occupation == f'{index}':
                user.occupation = occupation[f'{index}']
    return moveis, users

    print(users[0].occupation)
    print(users[5].occupation)
    print(users[15].occupation)
    print(moveis[1].id)
    print(users[4].user_id)
    print(users[150].user_gender)


def read_files():
    folder_path = "D:\\Sina\\Pyhton\\Python\\homeworks\\hw5\\film\\"

    files_dict = {}

    files = glob.glob(os.path.join(folder_path, '*.txt'))

    for file_path in files:
        with open(file_path, 'r') as file:


            file_name = os.path.splitext(os.path.basename(file_path))[0]

            files_dict[file_name] = f"{file.read()}"

    return files_dict


def stage_2():
    read_files()


def stage_3():
    current_contents = read_files()
    current_movies, current_users = stage_1_step_1()
    common_list = []

    for contents in current_contents:
        words = current_contents[contents]
        for movie in current_movies:
            a = movie.title
            searchs =re.sub(r'\(.*?\)', "", a)
            if re.search(searchs,words):
                common_list.append(movie.title)
            else:
                with open('review.txt', 'a') as file:
                    file.write(f'{movie.title} Steal Little  is not found in folder {movie.link}\n')

    my_set = set(common_list)

    # Convert the set back to a list
    common_list = list(my_set)

    print(common_list)
def stage_4():
    with open('example.html', 'w') as f:
        # Write HTML code to the file
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Example Page</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<h1>Hello, World!</h1>\n')
        f.write('</body>\n')
        f.write('</html>\n')


stage_3()
