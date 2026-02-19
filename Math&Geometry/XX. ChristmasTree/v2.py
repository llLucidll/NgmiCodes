def christmasTree(h: int) -> None:
    width = h * 2 - 1
    padding = width - 1

    for i in range(1, width + 1, 2):
        print(" " * (padding//2), end='')
        print("*" * i)
        padding = padding - 2

christmasTree(4)