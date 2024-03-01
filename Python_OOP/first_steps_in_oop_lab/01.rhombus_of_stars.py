def print_rhombus(size):
    for row in range(1, size + 1):
        print(f"{' '*(size - row)}{'* '*row}")

    for row in range(size - 1, 0, -1):
        print(f"{' '*(size - row)}{'* '*row}")


n = int(input())
print_rhombus(n)
