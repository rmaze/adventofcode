from itertools import product
import sys
from multiprocessing import Pool, cpu_count


def eval_equation(numbers, ops):
    result = numbers[0]
    for op, num in zip(ops, numbers[1:]):
        if op == "+":
            result += num
        elif op == "*":
            result *= num
        elif op == "||":
            result = int(str(result) + str(num))
    return result


def equation_possible(args):
    target, numbers = args
    operators = product(["+", "*", "||"], repeat=len(numbers) - 1)
    return any(eval_equation(numbers, ops) == target for ops in operators)


def main():
    tasks = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        target, nums = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, nums.strip().split()))
        tasks.append((target, numbers))

    with Pool(cpu_count()) as pool:
        results = pool.map(equation_possible, tasks)

    calibration_sum = sum(target for (target, _), valid in zip(tasks, results) if valid)
    print(calibration_sum)


if __name__ == "__main__":
    main()
