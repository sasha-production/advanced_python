import sys


def get_mean_size(ls_output) -> float:
    total, count = 0, 0
    if not ls_output:
        return 'файлов нет'
    for file in ls_output:
        try:
            total += int(str(file.split()[4]))
        except:
            return 'не удается получить размер файла'
        count += 1
    mean_size = total / count
    return mean_size


if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    mean_size = get_mean_size(lines)
    print(mean_size)
    