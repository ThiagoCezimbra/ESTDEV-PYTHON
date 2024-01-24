def lernotas():
    nota1 = float(input('Digite a nota do trimestre: '))
    return nota1

def calcularMedia(n1,n2):
    media = (n1+n2)/2
    return media



a = lernotas()
b = lernotas()
calc = calcularMedia(a,b)

if (calcularMedia(a,b)>= 7):
    print('Aprovado')
else:
    print('Reprovado')
