import math
primes = []
tope = int(inputbox("Ingrese el limite: "))
for a in range((tope % 2) + (math.trunc(tope / 2))):
    acumulador = 0
    cont = 1
    if a == 0:
        numero = 2
    else:
        numero = 2 + ((a * 2) - 1)
    a_str = str(numero)
    if a_str[len(a_str) - 1] == "5" and numero != 5:
        cont = 0
    else:
        cont = 1
        for value in range(len(primes) - 1):
            if numero % primes[value + 1] == 0:
                cont = 0
                break
            if primes[value + 1] >= numero / primes[value]:
                cont = 1
                break
    if cont != 0:
        primes.append(numero)
for a in range(len(primes)):
    print(a + 1 , ". " , primes[a])
#Tarda ~1,5s para 20.000
#tarda ~6s para 100.000
#Tarda ~20s para 1.000.000
#Tarda ~264 s para 10.000.000
#Tarda ~22426 s para 100.000.000

#datos basados en la velocidad de mi pc
