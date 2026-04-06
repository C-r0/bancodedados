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
print("So é permitido 2 digitos, se você querer acessar o 6 digite 20,\nse você quiser acessar o 1 digite 11, \nnão tem necessidade do 0 quando o numero for na ultima linha")
res = int(input("Endereço: "))
u = res // 1 % 10
d = res // 10 % 10
if(d == 0):
    print("Bloco 4", b4)
elif(d == 2):
    if(u == 1):
        print("Bloco 5", b5)
    elif(u == 2):
        print("Bloco 7", b7)
    elif(u == 0):
        print("Bloco 6", b6)
elif(d == 1):
    if(u == 1):
        print("Bloco 1", b1)
    elif(u == 2):
        print("Bloco 3", b3)
    elif(u == 0):
        print("Bloco 2", b2)
input()
