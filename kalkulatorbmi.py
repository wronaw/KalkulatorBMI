def okresl_bmi():
    masa = int(input("Podaj mase(w kg): "))
    wzrost = int(input("Podaj wzrost(w cm): "))
    bmi = (masa / (wzrost**2)) * 10000
    return bmi


def main():
    bmi = okresl_bmi()
    print("Twoje BMI  to:", bmi)
    if bmi < 16:
        print("Według BMI jesteś wygłodzony")
    elif (bmi >= 16) and (bmi <= 16.99):
        print("Według BMI jesteś wychudzony")
    elif (bmi >= 17) and (bmi <= 18.49):
        print("Według BMI masz niedowagę")
    elif (bmi >= 18.5) and (bmi <= 24.99):
        print("Według BMI jesteś w normie")
    elif (bmi >= 25) and (bmi <= 29.99):
        print("Według BMI masz nadwagę")
    elif (bmi >= 30) and (bmi <= 34.99):
        print("Według BMI masz I stopień otyłości")
    elif (bmi >= 35) and (bmi <= 39.99):
        print("Według BMI masz II stopień otyłości (otyłość kliniczna)")
    elif bmi >= 40:
        print("Według BMI masz III stopień otyłości (otyłość skrajna)")
    else:
        print("Nieznany błąd")


main()
