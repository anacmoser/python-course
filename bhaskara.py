a= float(input("digite o valor do coeficiente A:"))
b= float(input("digite o valor do coeficiente B:"))
c= float(input("digite o valor do coeficiente C:"))

delta=b**2-4*a*c
if delta<0:
    print("esta equação não possui raízes reais")
elif delta==0:
    s1=(-b-delta**0.5)/(2*a)

    print("a raiz dupla desta equação é", s1)
else:
    s1=(-b-delta**0.5)/(2*a)
    s2=(-b+delta**0.5)/(2*a)

    print("as raízes da equação são", s1, "e", s2)
