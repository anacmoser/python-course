s1=input("Por favor, entre com o número de segundos que deseja converter:")

dias= (int(s1)//86400)
horast=(int(s1)%86400)
horas= horast//3600
s2=(int(s1)%3600)
minutos=s2//60
segundos=s2%60


print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")