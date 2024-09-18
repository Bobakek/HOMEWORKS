import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    try:

        with open(name, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                line = f.readline()
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
    filenames = [f'./file {number}.txt' for number in range(1, 4)] # Список файлов
    start = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)  # Запускаем функцию для каждого файла (3.1 секунды)
    finish = time.time()
    print(f"Время выполнения: {finish - start} секунд")

    filenames = [f'./file {number}.txt' for number in range(1, 4)] # Список файлов
    start = time.time()
    for file in filenames:
        read_info(file)
    finish = time.time()
    print(f"Время выполнения: {finish - start} секунд")

