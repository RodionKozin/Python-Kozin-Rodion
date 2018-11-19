easy.py
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import sys
path_dir =[('dir_' + str(i + 1)) for  i in range(9)]
 
def make_dir(paths):
    dir_path = os.path.join(os.getcwd(),paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')
 
for i in path_dir:
    make_dir(i)
	
def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')	
 
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
 
list_dir(main_path)
 
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
 
def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)
 
 
def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')
  
Normal.py
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
 
import os
import easy
9
exitos ='a'
while exitos != '0':
    print('Перейти в папку - выбрать 1')
    print('Просмотреть содержимое текущей папки - выбрать 2')
    print('Удалить папку - выбрать 3')
    print('Создать папку - выбрать 4')
    print('для выхода - выбрать 0')
    exitos = input('Выберите действие: ' )
    print(exitos)
    if exitos == '1':
        dir_name = input ('ведите полный путь папки: ')
        easy.change_dir(dir_name)
    elif exitos == '2':
        dir_name = os.getcwd()
        easy.list_dir(dir_name)
    elif exitos == '3':
        dir_name = input('введите полный путь папки: ')
        easy.delete_dir(dir_name)
    elif exitos == '4':
        dir_name = input('ведите полный путь папки: ')
        easy.make_dir(dir_name)
    elif exitos == '0':
        pass
    else:
        print('Такой пункт в меню отсутствует')