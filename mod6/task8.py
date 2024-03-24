import re

number = input()
letters = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}


def search_words(numbers: str) -> list[str]:
    with open('words.txt', encoding='utf-8') as file:
        words = file.read()
        list_of_letters = ['[' + letters[x] + ']' for x in numbers]
        pattern = ''.join(list_of_letters)
        res = re.findall(f'\n{pattern}\n', words)
        return res


if __name__ == '__main__':
    possible_words = search_words(number)
    print(possible_words)