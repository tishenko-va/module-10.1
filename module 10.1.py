from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()
def write_words(word_count: int, file_name):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файлa {file}')


res1 = write_words(10, 'example1.txt')
res2 = write_words(30, 'example2.txt')
res3 = write_words(200, 'example3.txt')
res4 = write_words(100, 'example4.txt')


time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

time_start2 = datetime.now()

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)