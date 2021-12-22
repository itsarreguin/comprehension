import math

def main():
    square_root = {}

    for i in range(1, 1001):
        square_root[i] = math.sqrt(i)
    print(square_root)


if __name__ == '__main__':
    main()