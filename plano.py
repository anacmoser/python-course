x1=int(input("digite o primeiro valor x do plano cartesino"))
y1=int(input("digite o primeiro valor y do plano cartesino"))
x2=int(input("digite o segunndo valor x do plano cartesino"))
y2=int(input("digite o segundo valor y dddo plano cartesino"))

d=(((x1-x2)**2)+((y1-y2)**2))**0.5
if d>=10:
    print("longe")
else:
    print("perto")

