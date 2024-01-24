#senha três tentativas
n = 0
s = "w9wby"

while (n <= 3):

    print("tentativa nº: ",n + 1)
    n = n + 1
    senh = input("Digite sua senha")

    if (senh == s):
        print("Acesso concedido")

        break

    elif (n == 3):
        print("Favor recupere sua senha")
        break
