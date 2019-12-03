nums = []
tope = int(inputbox("Ingrese el tope: "))
for numero in range(tope+1):
    cont = 1
    for value in range(numero -2):
        if numero % (value + 2) == 0:
            cont = 0
            break
        if (value + 2) >= numero/(value + 1):
            cont = 1
            break
    if cont !=0 :
        nums.append(numero)
for a in range(len(nums) - 2):
    print(a + 1 , ". " , nums[a + 2])
#Tarda ~1,5s para 20.000
#Tarda ~53s para 1.000.000
#Tarda ~1140 s para 10.000.000
