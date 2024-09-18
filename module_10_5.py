import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    try:

        with open(name, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                all_data.append(line.strip())
                line = f.readline()
    except UnicodeDecodeError:
        try:

            with open(name, 'r', encoding='cp1252') as f:
                line = f.readline()
                while line:
                    all_data.append(line.strip())
                    line = f.readline()
        except UnicodeDecodeError:
            print(f"Ошибка чтения файла: {name}")
    return all_data

def process_files(file_paths):
    with Pool() as pool:
        results = pool.map(read_info, file_paths)
    return results

if __name__ == "__main__":
    path = r"C:\Users\Lenovo\IdeaProjects\untitled1\FILES"
    dir_list = os.listdir(path)

    # Преобразуем имена файлов в полный путь и фильтруем только файлы
    file_paths = [os.path.join(path, file) for file in dir_list if os.path.isfile(os.path.join(path, file))]

    #Проверяем, есть ли файлы в директории
    if file_paths:
        start = time.time()  # Начало замера времени

        # Обрабатываем файлы в многопроцессном режиме
        results = process_files(file_paths)

        end = time.time()  # Конец замера времени
        res = end - start  # Время выполнения: 6.75562596321106 секунд
        print(f"Время выполнения: {res} секунд")
    else:
        print("В директории нет файлов для чтения.")


    # if file_paths:
    #     start = time.time()  # Начало замера времени
    #
    #     # Линейно вызываем read_info для каждого файла
    #     for file in file_paths:
    #         read_info(file)
    #
    #     end = time.time()  # Конец замера времени
    #     res = end - start  # Разница времени  Время выполнения (линейно): 4.397747039794922 секунд
    #     print(f"Время выполнения (линейно): {res} секунд")
    # else:
    #     print("В директории нет файлов для чтения.")
