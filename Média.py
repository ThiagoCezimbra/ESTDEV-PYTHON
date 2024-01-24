notaA = float(input("Qual a nota da prova A? "))
notaB = float(input("Qual a nota da prova B? "))

media = (notaA + notaB) / 2

if media >= 7.0:
    print("Sua média é: %.1f aprovado"%media)
else:
    print("Sua média é: %.1f desaprovado" %media)