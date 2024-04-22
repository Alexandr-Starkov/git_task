'''Скрипт заменяет исходные слова в файлах на требуемые'''
import os

try:
    path = input('Введите путь к папке: ')
    files = os.listdir(path)
except FileNotFoundError:
    print('Такой папки не существует')
except NotADirectoryError:
    print('Указаный путь не является папкой')
else:
    txt_counter = 0
    txt_files = []

    for file in files:
        if '.txt' in file and not file.startswith('new'):
            txt_counter += 1
            txt_files.append(file)

    if txt_counter > 0:
        old_word = input(
            'Введите слово или словосочетание которое нужно заменить: ')
        new_word = input('Введите слово на которое нужно заменить: ')

        for file in txt_files:
            full_path = path + '\\' + file
            with open(full_path, 'r', encoding='utf-8') as f:
                old = f.readlines()

            with open(f'new_{file}', 'w', encoding='utf-8') as f:
                for i in old:
                    if 'черную кожаную курточку' in i.lower():
                        i = i.replace('черную кожаную курточку',
                                      'красную шапочку')
                    if old_word in i.lower():
                        i = i.lower().replace(old_word, new_word).title()
                        f.write(i)
                    else:
                        f.write(i)

    else:
        print('В папке нет текстовых файлов')
