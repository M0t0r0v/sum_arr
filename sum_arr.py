import sys


def count_elems(data, idx):
    count = 0
    for i in range(0, len(data) - 1):
        if data[idx] > data[i+1]:
            count += 1
    return count


def main():
    data = sys.stdin.readline().rstrip()
    data = data.split()
    kk = []
    for i in range(len(data)):
        cout = count_elems(data, i)
        kk.append(cout)
    return kk


if __name__ == '__main__':
    print(*main())
