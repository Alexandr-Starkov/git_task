'''Скрипт заменяет исходные слова в файлах на требуемые'''
import os


# Создаем папку output, если она не существует
os.makedirs('output', exist_ok=True)

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
            'Введите слово или словосочетание которое нужно заменить: ').strip().lower()
        new_word = input(
            'Введите слово на которое нужно заменить: ').strip().lower()

        for file in txt_files:
            # full_path = path + '\\' + file
            full_path = os.path.join(path, file)
            with open(full_path, 'r', encoding='utf-8') as f:
                old = f.readlines()

            # Создаем новый путь для сохранения файла в папке output
            output_file_path = os.path.join('output', file)
            with open(f'{output_file_path}', 'w+', encoding='utf-8') as f:
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
