peso=input("digite o peso")
altura=input("digite a altura")
imc=(float (peso))/(float ((altura)) ** 2)
imcint=int(imc)
if imc<=17.98:
    print("abaixo do peso, imc=", imcint)
elif 17.99<imc<24:
    print ("peso ideal, imc=", imcint)
else:
    print("acima do peso, imc=", imcint)