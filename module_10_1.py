import time
import threading
from time import sleep


def wite_words(word_count, file_name):
    with open(file_name, 'a') as f:
        for i in range(1, word_count + 1): f.write(f'какое-то слово №{i}')
        sleep(0.1)
    print(f'завершилась запись в файл {file_name}')


start_time = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time.time()
print(f'Time: {end_time - start_time}')

args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]
threads = []
for arg in args:
    thread = threading.Thread(target=wite_words, args=arg)
    threads.append(thread)

start_time = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
end_time = time.time()
print(f'Total time taken: {end_time - start_time} seconds')
