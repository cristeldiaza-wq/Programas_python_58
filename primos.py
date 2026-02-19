import argparse

parser = argparse.ArgumentParser()

parser.add_argument("n", type=int)

args = parser.parse_args()

n = args.n

if n <= 1:

    print("Ingrese un numero natural mayor que 1")

elif n == 2:

    print(f"El numero {n} es primo")

elif n % 2 == 0:

    print(f"El numero {n} es compuesto.\nSe cumple que 2 * {n//2} = {n}")

else:

    escompuesto = False

    divisor = 3

    while divisor * divisor <= n:

        if n % divisor == 0:

            escompuesto = True

            break

        divisor += 2

    if not escompuesto:

        print(f"El numero {n} es primo")

    else:

        print(f"El numero {n} es compuesto.\nSe cumple que {divisor} * {int(n/divisor)} = {n}")