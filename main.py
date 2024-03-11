import math
import time
from typing import NamedTuple


class T:
    def __init__(self, timer: time.time = 0.0, page_actual_main: int = 0, pages: int = 0):
        self.timer = timer
        self.page_actual_main = page_actual_main
        self.pages = pages


def backup(t: T):
    with open('../../backup.txt', 'a') as f:
        f.write(f"За {round(t.timer)} сек, я прочитал {t.pages} страниц. Это {int(t.pages / t.page_actual_main * 100)}% и осталось {t.page_actual_main}\n")
        print('Сделал запись. Цель окончена.\n\n\n\n')


def get_main_part() -> int:
    with open('../../backup.txt', 'r') as f:
        x = f.readlines()
    return int(x[-1].split()[-1])


def end_timer():
    while True:
        res = input('Окончить таймер. y?')
        if res.lower() == 'y':
            break


if __name__ == '__main__':
    all_part = 400
    print("Программа начала работу.")
    t = T(page_actual_main=get_main_part())
    print(f'Ты остановился на: {all_part - t.page_actual_main}')

    try:
        while True:
            i = input('Введите количество страниц, которое собираетесь прочитать: ')
            start = time.time()
            if i == '0':
                break
            if i.isdigit():
                t.pages = int(i)
                print(f'Вы должны остановиться на {all_part - t.page_actual_main + t.pages} странице.')
                end_timer()
                t.timer = time.time() - start
                t.page_actual_main -= t.pages
                backup(t=t)

    except KeyboardInterrupt as e:
        print(e)
        backup(t)
    except Exception as e:
        print(e)
        backup(t)
