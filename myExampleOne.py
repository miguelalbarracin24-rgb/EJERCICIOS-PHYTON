def validNumber():
     
    while True:
        entrada = input("Ingrese un número: ")
        try:
            numero = float(entrada)
            break  # Salir del ciclo si la conversión fue exitosa
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido.")
 
    # Clasificar el número usando condicionales
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.") 



def main():
    validNumber()



if __name__ == "__main__":
    main()