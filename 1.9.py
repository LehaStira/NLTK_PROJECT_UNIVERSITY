def lists_generation_demonstration():  # 1.9
    result = [i ** 2 for i in range(1, 100) if i % 10 == 5]
    return result


def main():
    res = lists_generation_demonstration()
    print(res)


if __name__ == '__main__':
    main()