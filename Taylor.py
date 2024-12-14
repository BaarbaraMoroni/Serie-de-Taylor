import math


def taylor_ex(x, n):
    
    result = 0
    for i in range(n):
        result += x**i / math.factorial(i)
    return result


def main():
    x = float(input("Digite o valor de x: "))
    n = int(input("Digite o número de termos da série (n): "))


    ex_direct = taylor_ex(x, n)


    if x < 0:
        y = -x
        ex_y = taylor_ex(y, n)
        ex_inverse = 1 / ex_y


        print(f"Cálculo de e^x diretamente: {ex_direct}")
        print(f"Cálculo de e^x usando y = -x e 1/e^x: {ex_inverse}")
    else:
        print(f"Cálculo de e^x diretamente: {ex_direct}")


if __name__ == "__main__":
    main()



