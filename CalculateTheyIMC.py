# solicitar datos de peso y altura al usuario

def calculateTheyIMC():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Error: Height must be greater than zero.")
                continue
            break  # Exit the loop if the conversion was successful
        except ValueError:
            print("Error: Please enter a valid numeric value.")
        
    imc = weight / (height ** 2)
    print(f"Your Body Mass Index (BMI) is: {imc:.2f}")

    if imc < 18.5:
        print("You are underweight.")
    elif 18.5 <= imc < 24.9:
        print("You have a normal weight.")
    elif 25 <= imc < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

def main():
    calculateTheyIMC() 


if __name__ == "__main__":
    main()