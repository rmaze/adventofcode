from itertools import product
import sys


def eval_equation(numbers, ops):
    result = numbers[0]
    for op, num in zip(ops, numbers[1:]):
        if op == "+":
            result += num
        else:
            result *= num
    return result


def equation_possible(target, numbers):
    # Generate all combinations of '+' and '*'
    operators = product(["+", "*"], repeat=len(numbers) - 1)
    return any(eval_equation(numbers, ops) == target for ops in operators)


def main():
    calibration_sum = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        target, nums = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, nums.strip().split()))

        if equation_possible(target, numbers):
            calibration_sum += target

    print(calibration_sum)


if __name__ == "__main__":
    main()
