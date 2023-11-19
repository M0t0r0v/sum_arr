import sys


# Функция подсчёта элементов
def count_elems(data, idx):
    # инициализация счётчика
    count = 0
    # цикл для сравнения элементов
    for i in range(0, len(data)):
        # print(f'{data[idx]} > {int(data[i])}')  # для отладки
        if int(data[idx]) > int(data[i]):
            count += 1
        count = count     
    return count


def main():
    # входные данные
    data = sys.stdin.readline().rstrip()
    # по пробелам в список
    data = data.split()
    # инициализация списка сумм накопленных сравнений
    sum_of_elements = []
    # цикл для подсчёта суммы и записи результат в список
    for i in range(len(data)):
        sum_of_elements.append(count_elems(data, i))
    return sum_of_elements


if __name__ == '__main__':
    print(*main())
