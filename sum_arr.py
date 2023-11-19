import sys


# Функция подсчёта элементов
def count_elems(data, idx):
    # инициализация счётчика
    count = 0
    # цикл для сравнения элементов
    for i in range(0, len(data)):
        print(f'{data[idx]}>{data[i]}')  # для отладки
        if data[idx] > data[i]:
            count += 1
    return count


def main():
    # входные данные
    data = sys.stdin.readline().rstrip()
    # по пробелам в список
    data = data.split()
    # инициализация списка сумм накопленных сравнений
    sum_of_elements = []
    # цикл для каждого элемента
    for i in range(len(data)):
        cout = count_elems(data, i)
        sum_of_elements.append(cout)
    return sum_of_elements


if __name__ == '__main__':
    print(*main())
