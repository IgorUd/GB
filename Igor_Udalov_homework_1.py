# Task 1. Creating the program that can transfer amount of seconds in format days/hours/minutes/seconds.

duration = int(input('Введите количество секунд: '))

days = duration // 86400
hours = (duration // 3600) % 24
minutes = (duration // 60) % 60
sec = duration % 60

print(str(days) + ' дн ' + str(hours) + ' час ' + str(minutes) + ' мин ' + str(sec) + ' сек')


# Task 2.

# Creating the function.
def homework(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res


# Creating the massive from 1 to 1001 with step of 2, to exclude even numbers.

arr = [n ** 3 for n in range(1, 1001, 2)]

# We output two types of results by filtering numbers with a lambda function that are not divisible by 7 without
# remainder.

answer1 = sum(filter(lambda num: homework(num) % 7 == 0, arr))
answer2 = sum(filter(lambda num: homework(num + 17) % 7 == 0, arr))

print(answer1)
print(answer2)

# Task 3.

# Creating a variable that includes exception numbers.

numbers = {11, 12, 13, 14}

# Creating a list with cycle "for", and we assign the necessary declension to each value.

for i in range(100):
    i = i + 1
    if i in numbers:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif 1 < i % 10 < 5:
        print(i, "процента")
    else:
        print(i, "процентов")
