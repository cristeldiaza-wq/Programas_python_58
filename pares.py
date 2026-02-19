import argparse
#crear un parser (generador sintactico: puente de comunicacion terminal con python)
parser = argparse.ArgumentParser()
parser.add_argument("n", type = int)

#Traducir de lo que escriba de la terminal a python
args = parser.parse_args()

#codigo de calculo 
n = args.n
for i in range (1, n *2+1):
    if i%2== 0:
        print(i)
