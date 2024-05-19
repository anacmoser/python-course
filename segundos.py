s1=input("Digite a quantidade de segundos")

horas=(int(s1)//3600)
s2=(int(s1)%3600)
minutos=s2//60
segundos=s2%60

print(horas, "horas,", minutos, "minutos e", segundos, "segundos.")