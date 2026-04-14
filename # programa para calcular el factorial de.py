# programa para calcular el factorial de un numero

num = int(input("Ingrese un numero: "))
factorial = 1

#verificacion de numeros positivos
if num < 0:
    print("No se puede calcular el factorial de los numeros negativos")

elif num == 0:
    print("El factorial de 0 es 1.")    
else:
    #uso ciclo for para calcular el factorial    
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"El factorial de {num} es {factorial}")