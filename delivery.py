from typing import List


def min_platforms(robot_weight: List[int], limit: int) -> int:
    """
    Функция для подсчета минимального количества платформ
    для перевозки роботов
    """
    left_pointer = 0
    right_pointer = len(robot_weight) - 1
    platforms = 0

    while left_pointer <= right_pointer:
        result = (
            robot_weight[left_pointer] +
            robot_weight[right_pointer]
        )
        if result <= limit:
            left_pointer += 1
        platforms += 1
        right_pointer -= 1
    return platforms


if __name__ == '__main__':
    robot_weight = [int(weight) for weight in input().split()]
    limit = int(input())
    robot_weight.sort()
    print(min_platforms(robot_weight, limit))
