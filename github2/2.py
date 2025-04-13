ct = 0
aprovado = 0
reprovado = 0
print("digite [0] para sair: ")
while True:
    valor = int(input(" digite a nota: "))
    if valor == 0:
        break
    ct = ct +1
    if valor >= 5:
        aprovado += 1
    if valor < 5:
        reprovado + 1
print("a quantidade de alunos que fizeram a prova é: ", ct)            
print("a quantidade de alunos que foram aprovados é: ", aprovado)            
print("a quantidade de alunos que foram reprovados é: ", reprovado)            