# ID посылки 108249317
import string


def decode(encode: str):
    temp_code: list[tuple] = []
    current_num: str = ""
    current_str: str = ""
    for value in encode:
        if value in string.digits:
            current_num += value
        elif value == '[':
            temp_code.append((int(current_num), current_str))
            current_num = ""
            current_str = ""
        elif value == ']':
            last_num, last_str = temp_code.pop()
            current_str = last_str + current_str * last_num
        else:
            current_str += value
    return current_str


if __name__ == '__main__':
    print(decode(input()))
