import datetime
import random
import uuid

list1 = [
    ['ali', 1001],
    ['sina', 1002],
    ['rasit', 1003]

]
dict1 = {
    'ali': 1001,
    'sina': 1002,
    'rasit': 1003

}

for i in range(1000000):
    my_name = uuid.uuid4()
    random_number = random.randint(100_000, 500_000)
    dict1[my_name] = random_number
    list1.append([my_name, random_number])

looking_value = list1[-1][0]

start = datetime.datetime.now()
for i in list1:
    if i[0] == looking_value:
        print(f"my_name: {i[0]}, value: {i[1]}")

end = datetime.datetime.now()

print(f"my_name: {looking_value}, value: {dict1[looking_value]}")

end_2 = datetime.datetime.now()

print(end - start)
print(end_2 - end)
