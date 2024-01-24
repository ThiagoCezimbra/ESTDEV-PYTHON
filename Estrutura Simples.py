A = input("Informe um valor para a variável A ")
B = input("Informe um valor para a variável B ")

if (A > B):
    aux=A;
    A=B;
    B=aux;
    print("O valor de é A agora é: ", A)
    print("O valor de B agora é: ", B)
else:
    print("Estragou a brincadeira")
