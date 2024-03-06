import sys


def decrypt(encryption: str) -> str:
    stack = []
    for c in encryption:
        stack.append(c)
        if len(stack) > 2 and stack[-2:] == ['.', '.']:
            del stack[-1]
            del stack[-1]
            if stack:
                del stack[-1]
    return ''.join(filter(lambda x: x != '.', stack))


if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption)