'''Скрипт заменяет исходные слова в файлах на требуемые'''
import os

try:
    files = os.listdir(input('Введите путь к папке: '))
except FileNotFoundError:
    print('Такой папки не существует')
except NotADirectoryError:
    print('Указаный путь не является папкой')
else:
    txt_counter = 0
    txt_files = []

    for file in files:
        if '.txt' in file:
            txt_counter += 1
            txt_files.append(file)
            
    if txt_counter > 0:
        old_world = 'черная курточка'
        new_world = 'красная шапочка'
        
        
        for file in files:
            pass
    else:
        print('В папке нет текстовых файлов')
