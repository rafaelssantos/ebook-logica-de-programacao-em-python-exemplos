total_em_segundos = int(input("Informe o total em segundos: "))

dias = total_em_segundos // 86400 #Segundos que cabem em dia inteiro
resto_do_dia_em_segundos = total_em_segundos % 86400

horas = resto_do_dia_em_segundos // 3600 #Segundos que cabem na hora inteira
resto_da_hora_em_segundos = resto_do_dia_em_segundos % 3600

minutos = resto_da_hora_em_segundos // 60 #Segundo que cabem em minuto inteiro
segundos = resto_da_hora_em_segundos % 60

print(dias, "dia(s)", horas, "hora(s)", minutos, "minuto(s)", segundos, "segundo(s)")