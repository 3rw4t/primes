nums = []
tope= 23
for numero in range(tope+1):
    cont = 1
    for value in range(numero - 2):
        if numero % (value + 2) == 0:
            cont = 0
            break
    if cont != 0:
        nums.append(numero)
for a in range(len(nums) - 2):
    print(a + 1 , ". " , nums[a + 2])
#Tarda ~7s para 20.000
