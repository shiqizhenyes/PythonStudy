if __name__ == '__main__':
    print("******九九乘法表*******")
    factor_a = 1
    factor_b = 1
    while factor_a < 10:
        while factor_b <= factor_a:
            print(factor_b, "*", factor_a, "=", factor_a * factor_b, end="")
            factor_b += 1
            print(" ", end="")
        factor_b = 1
        factor_a += 1
        print("\n", end="")



