def collatz_for_n(n):
    # n %2 /2
    # n*3+1
    steps = 0
    while n != 1:
        print(round(n))
        steps += 1
        if (n % 2) == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    return steps


def run_10000000():
    max_steps = 0
    number_max_steps = 0
    for i in range(1, 1000000):
        steps = collatz_for_n(i)
        if steps > max_steps:
            max_steps = steps
            number_max_steps = i

    print(max_steps)
    print(number_max_steps)


if __name__ == '__main__':
    collatz_for_n(9)
