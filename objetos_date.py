import datetime

d = datetime.date(2024, 9, 16)

print(d)

from datetime import date, datetime, time # forma mais utilizada
data = date(2024, 9, 16)

print(data)

print(date.today()) #pega o dia atual

data_hora = datetime(2024, 9, 16, 10, 1, 10) #retorna com data, hora, minuto e segundo

print(data_hora)
print(datetime.today())

hora = time(10, 41, 0)
print(hora)
