def diamond_pattern(rows: int):
    print("\nBelow is the diamond pattern\n")
    # Parte superior
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    # Parte inferior
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


diamond_pattern(10)