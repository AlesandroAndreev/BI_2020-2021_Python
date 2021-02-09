#_________________________Functions___________________________


def ex_1(numbers_of_points = 1000):

    import random
    import numpy
    import time
    import matplotlib.pyplot as plt

    numbers_count = []

    time_random = []
    time_numpy = []

    for i in range(numbers_of_points):
        start_point = time.time()

        numbers_count.append(i)

        for j in range(i):
            random.randint(0,1)

        end_point = time.time()

        time_random.append(end_point - start_point)

        start_point = time.time()

        numpy.random.uniform(0, 1, i)

        end_point = time.time()

        time_numpy.append(end_point - start_point)

    plt.plot(numbers_count, time_random, label = "Time with use random")
    plt.plot(numbers_count, time_numpy, label = "Time with use numpy")
    plt.xlabel('Iteration numbers')
    plt.ylabel('Time')
    plt.title('Graph comparing running times of random.random and numpy.random')
    plt.legend()
    plt.show()


def ex_2(numbers_of_points = 9):

    import random
    import numpy
    import time
    import matplotlib.pyplot as plt

    def is_sorted(lst, key=lambda x: x):
        for i, el in enumerate(lst[1:]):
            if key(el) < key(lst[i]):
                return False
        return True

    def monkey_sort(list_of_numbers):



        while not is_sorted(list_of_numbers):
            random.shuffle(list_of_numbers)
        return list_of_numbers

    def create_vizualize():

        import statistics

        vector = []

        time_vector = []

        time_dispersion_vector = []

        for i in range(1, numbers_of_points + 1):

            vector.append(i)
            time_seria = []

            for j in range(10):

                start_point = time.time()

                monkey_sort(numpy.random.randint(1,100,i))

                end_point = time.time()

                time_seria.append(end_point - start_point)

            time_vector.append(statistics.mean(time_seria))
            time_dispersion_vector.append(statistics.pvariance(time_seria))

        plt.plot(vector, time_vector, label = "Mean")
        plt.plot(vector, time_dispersion_vector, label = "Dispersion")
        plt.xlabel('List length')
        plt.ylabel('Time')
        plt.title('The graph of the running time of the monkey sorting algorithm depending on the size of the list')
        plt.legend()

        plt.show()

    create_vizualize()

def ex_3( n = 10000):

    import numpy
    import matplotlib.pyplot as plt
    import random

    x = numpy.zeros(n)
    y = numpy.zeros(n)

    for i in range(1, n):

        val = random.randint(1, 4)

        if val == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1


    plt.scatter(x, y)
    plt.xlabel("Step x")
    plt.ylabel("Step y")
    plt.title("Random Walk ($n = " + str(n) + "$ steps)")
    plt.show()


def ex_4(numbers_of_points = 10000):

    import random
    import matplotlib.pyplot as plt

    def plot_triangle(points):

        x_vector = [x for (x, y) in points]
        y_vector = [y for (x, y) in points]

        plt.plot(x_vector, y_vector, 'b^')
        plt.title("Sierpinski triangle")
        plt.show()


    def sierpinski_triangle(n):

        vertices = [(0.0, 0.0), (0.5, 0.5), (1.0, 0.0)]
        points = []

        x, y = random.choice(vertices)

        for i in range(n):

            vx, vy = random.choice(vertices)

            x = (vx + x) / 2.0
            y = (vy + y) / 2.0

            points.append((x, y))

        plot_triangle(points)

    sierpinski_triangle(numbers_of_points)

def ex_5():

    import random
    import os


    def mix_in_word(word):

        word = list(word)
        start = word[0]

        if word[len(word) - 1] in [",", ".", "\'", "\"", ";","\n"]:
            body_to_mix = word[1:len(word) - 2]
            end = word[len(word) - 2 : len(word)]
        else:
            end = word[len(word) - 1]
            body_to_mix = word[1:len(word) - 1]

        random.shuffle(body_to_mix)

        return "".join([*start, *body_to_mix, *end])

    way_input = input("Enter path to original text: ")
    name, extension = os.path.splitext(way_input)
    way_output = name + "_shuffling" + extension

    original_text = open(way_input ,'r', encoding='cp1251')
    shuffling_text = open(way_output,'w', encoding='cp1251')

    for line in original_text:
        for shuffling_word in line.split():
            if len(shuffling_word) > 1:
                shuffling_text.write(mix_in_word(shuffling_word) + " ")
            else:
                shuffling_text.write(shuffling_word+ " ")


def ex_6(levels = 6):

    import numpy as np
    import matplotlib.pyplot as plt


    def create_square(x_square, y_square, size_of_square, figure):

        for i in range(x_square, x_square + size_of_square):
            for j in range(y_square, y_square + size_of_square):
                figure[i, j] = 0
        return figure



    size = 3**levels

    img = np.ones((size, size), dtype=np.uint8)

    for level in range(1, levels+1):
        square_size = int(size/(3**level))
        for x in range(0, 3**level, 3):
            x = int((x+1)*square_size)
            for y in range(0, 3**level, 3):
                y = int((y+1)*square_size)
                img = create_square(x, y, square_size, img)


    plt.axis('off')
    plt.title("Sierpinski carpet")
    plt.imshow(img, cmap='binary')
    plt.show()

#_________________________Body___________________________

print(" Данная работа посвящена применению модулей Random и Pandas для решения разного рода задач в програмировании")
print("Для того чтобы протестировать функцию введите ее номер !")
print(" 1 - Сравнение скорости работы модулей Random и Numpy")
print(" 2 - Демонстрация скорости работы алгоритма monkey sort")
print(" 3 - Визуализация random walk в 2-мерном пространстве")
print(" 4 - Треугольник Серпинского")
print(" 5 - Текст с перепутанными буквами - необходимо ввести путь до рабочего файла. Кодировка cp1251")
print(" 6 - Коврик Серпинского")
print("Для рассмотрения сразу нескольких заданий можно ввести номера через пробел")

number_of_the_task = [num for num in input().split()]

for number in number_of_the_task:
    if number == "1":
        ex_1()
    elif number == "2":
        ex_2()
    elif number == "3":
        ex_3()
    elif number == "4":
        ex_4()
    elif number == "5":
        ex_5()
    elif number == "6":
        ex_6()
