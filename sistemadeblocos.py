b1 = "x = 10"
b2 = "Nome = Joao"
b3 = "cor = azul"
b4 = "y = 11"
b5 = "user = admin"
b6 = "pass = 12345"
b7 = "token = 123123"
print("Blocos com dados:")
print("     4     ")
print("  2     6  ")
print("1   3  5  7")
print("1 = Esquerda, 2 = Direita, 0 = Ler bloco atual")
res = int(input("Comando: "))
if res == 0:
    print("Dados bloco 4:")
    print(b4)
if res == 1:
    print("Agora você esta no bloco 2")
    res = int(input("Comando: "))
    if res == 0:
        print("Dados Bloco 2:")
        print(b2)
    if res == 1:
        print("Dados Bloco 1:")
        print(b1)
    if res == 2:
        print("Dados Bloco 3:")
        print(b3)
    exit()
if res == 2:
    print("Agora você esta no bloco 6")
    res = int(input("Comando: "))
    if res == 0:
        print("Dados Bloco 6:")
        print(b6)
    if res == 1:
        print("Dados Bloco 5:")
        print(b5)
    if res == 2:
        print("Dados Bloco 7:")
        print(b7)
