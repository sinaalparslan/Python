def calculation_mean(row: list) -> object:
    """

    :param row: every line for date
    :return:alp_score for calculation of mean values
    """
    row = row[:-1]

    score_list = row.split(':')

    student = score_list[0]
    score = score_list[1].split(',')

    first_score = int(score[0])
    second_score = int(score[1])
    third_score = int(score[2])

    mean_value = (first_score + second_score + third_score) / 3
    value = cal_alp(mean_value, student)
    return value


def cal_alp(mean, stu):
    """

    :param mean: mean score
    :param stu: student name
    :return: alp_score
    """
    if mean > 90:
        alp_score = "AA"
    elif mean > 80:
        alp_score = "BA"
    elif mean > 70:
        alp_score = "BC"
    elif mean > 60:
        alp_score = "CA"
    elif mean > 50:
        alp_score = "CC"
    elif mean > 40:
        alp_score = "DC"
    else:
        alp_score = "FF"
    return stu + ":" + alp_score + "\n"


def mean_score():
    """

    :return: mean score
    """
    with open("Exam_score.txt", "r") as file:
        for i in file:
            print(calculation_mean(i))


def enter_score():
    """

    :return: write file
    """
    name = input("Student's name : ")
    surname = input("Student's surname : ")
    first_score = input("Student's first score: ")
    second_score = input("Student's second score : ")
    third_score = input("Student's third score : ")

    with open("Exam_score.txt", "a") as file:
        file.write(name + ' ' + surname + ':' + first_score + ',' + second_score + ',' + third_score + '\n')


def save_score():
    """

    :return: Exam_score.txt file and Result_score.txt file
    """
    with open('Exam_score.txt', 'r') as file:
        result_list = []
        for i in file:
            result_list.append(calculation_mean(i))

        with open('Result_score.txt', "w") as file2:
            for j in result_list:
                file2.write(j)


def main():
    """
    this function that can enter  student name, surname and grades.
    its calculation the overage of grades,determine the letter grades and its saved all information
    :return:
    """
    while True:
        process = input('1-Read Score\n2-Enter Score\n3-Save Score\n4-Exit\n')

        if process == '1':
            mean_score()
        elif process == '2':
            enter_score()
        elif process == '3':
            save_score()
        else:
            break


main()
