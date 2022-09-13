from django.shortcuts import render
import random

muscle_group = ''


def exercises():

    """Открывает файл, разделяет данные по запятой, создает случайный список упражнений."""

    with open(f'data/{muscle_group}.txt', "r", encoding="utf-8") as f:
        read_file = f.read()

    split_exercise = read_file.split(",")

    random.shuffle(split_exercise)

    i = 0
    final_list = []

    for el in split_exercise:
        final_list.append(el)
        i += 1
        if i == 4:
            break

    return final_list


def main(request):
    return render(request, 'mainapp/index.html')


def back(request):
    global muscle_group

    muscle_group = 'спина'

    content = {
        'title': 'спина',
        'exercises': exercises()
    }
    return render(request, 'mainapp/back.html', context=content)


def biceps(request):
    global muscle_group

    muscle_group = 'бицепс'

    content = {
        'title': 'бицепс',
        'exercises': exercises()
    }
    return render(request, 'mainapp/biceps.html', context=content)


def breast(request):
    global muscle_group

    muscle_group = 'грудь'

    content = {
        'title': 'грудь',
        'exercises': exercises()
    }
    return render(request, 'mainapp/breast.html', context=content)


def legs(request):
    global muscle_group

    muscle_group = 'ноги'

    content = {
        'title': 'ноги',
        'exercises': exercises()
    }
    return render(request, 'mainapp/legs.html', context=content)


def press(request):
    global muscle_group

    muscle_group = 'пресс'

    content = {
        'title': 'пресс',
        'exercises': exercises()
    }
    return render(request, 'mainapp/press.html', context=content)


def shoulders(request):
    global muscle_group

    muscle_group = 'плечи'

    content = {
        'title': 'плечи',
        'exercises': exercises()
    }
    return render(request, 'mainapp/shoulders.html', context=content)


def triceps(request):
    global muscle_group

    muscle_group = 'трицепс'

    content = {
        'title': 'трицепс',
        'exercises': exercises()
    }
    return render(request, 'mainapp/triceps.html', context=content)
