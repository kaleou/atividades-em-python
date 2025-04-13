ct_par = 0
ct_impar = 0
par = 0
impar = 0
print("digite [0] para sair:")
while True:
    valor = int(input("digite um numero: "))
    if valor == 0:
        break
    if valor % 2 == 0:
        par += valor
        ct_par +=1
    else:
        impar += valor
        ct_impar += 1
print("a media aritimetica de numeros pares é: ", par / ct_par)
print("a media aritimetica de numeros impares é: ", impar/ ct_impar)
