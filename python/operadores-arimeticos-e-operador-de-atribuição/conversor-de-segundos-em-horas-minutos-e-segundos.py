total_em_segundos = 4000
horas = total_em_segundos // 3600
resto_da_hora = total_em_segundos % 3600
minutos = resto_da_hora // 60
segundos = resto_da_hora % 60
print(horas, "hora(s)", minutos, "minuto(s)", segundos, "segundo(s).")