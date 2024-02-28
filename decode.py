# ID посылки 108249317
import string


def decode(encode: str):
    temp_code: list[tuple] = []
    current_num: str = ''
    current_exp: str = ''
    for value in encode:
        if value in string.digits:
            current_num += value
        elif value == '[':
            temp_code.append((int(current_num), current_exp))
            current_num = ''
            current_exp = ''
        elif value == ']':
            last_num, last_str = temp_code.pop()
            current_exp = last_str + current_exp * last_num
        else:
            current_exp += value
    return current_exp


if __name__ == '__main__':
    print(decode(input()))
