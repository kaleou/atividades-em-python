ct = 0
soma = 0
Mvinte = 0
print("digite [-1] para sair")
while True:
    numero = int(input("digite um numero: "))
    if numero == -1:
        break
    ct = ct + 1
    soma = numero + soma     
    media = soma / ct
    if numero > 20: Mvinte = Mvinte + 1       
print("a quantidade de numeros é: ", ct )
print("a soma dos numeros é: ", soma)
print("a media é:", media)
print(f"a quantidade de valores digitados maior que 20 é {Mvinte};")
    
