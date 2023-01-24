import random

list1 = []
for i in range(1000):
    random_number = random.randint(1, 5000)

    list1.append(random_number)
list1.sort()
num = list1[len(list1) - 25]
print(num)


def find_num(list, num):
    low_num = 0
    upp_num = len(list) - 1
    while (list[low_num] <= list[upp_num]):
        mid_num = (low_num + upp_num) // 2
        if list[mid_num] < num:
            low_num = mid_num + 1
        elif list[mid_num] > num:
            upp_num = mid_num - 1
        else:
            return mid_num


find_num(list1, num)
