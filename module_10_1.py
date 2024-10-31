import time
import threading
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


word_counts = [10, 30, 200, 100]
# запись в файлы без потоков
started_at = time.time()
for i, word_count in zip(range(0, 4), word_counts):
    write_words(word_counts[i], f'example{i+1}.txt')

ended_at = time.time()
print(f'Запись завершена за {round(ended_at - started_at, 2)} секунд')
# запись в файлы с потоками
started_at = time.time()
threads = []
for i in range(0, 4):
    t = threading.Thread(target=write_words, args=(word_counts[i], f'example{i+5}.txt'))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
ended_at = time.time()
print(f'Запись завершена за {round(ended_at - started_at, 2)} секунд')
