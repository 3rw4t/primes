import math
def primes(tope):
    vector = []
    for a in range((tope % 2) + (math.trunc(tope/2))):
        acumulador = 0
        cont = 1
        if a == 0:
            numero = 2
        else:
            numero = 2 + ((a * 2) - 1)
        a_str = str(numero)
        if a_str[len(a_str)-1] == "5" and numero != 5:
            cont = 0
        else:
            cont = 1
            for value in range(len(vector )-1):
                if numero % vector[value+1] == 0:
                    cont = 0
                    break
                if vector[value+1] >= numero/vector[value]:
                    cont = 1
                    break
        if cont !=0 :
            vector.append(numero)
    return vector
"""
vecprimes = primes(1000)                              #ejemplo de uso con los primos entre 0 y 1000
for a in range(len(vecprimes)):
    print("{}. {}".format(a + 1, vecprimes[a]))
"""

#Tarda ~1,5s para 20.000
#tarda ~6s para 100.000
#Tarda ~20s para 1.000.000
#Tarda ~264 s para 10.000.000
#Tarda ~22426 s para 100.000.000

#datos basados en la velocidad de mi pc
