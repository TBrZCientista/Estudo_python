import datetime

d = datetime.datetime.now()

print(d.strftime("%d/%m/%Y %H:%M")) # Formatando a data e hora

date_string = "16/9/2024 11:23"

d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M") #convertendo string pra datetime

print(d)

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2024-09-16 13:10'
mascara_ptbr = "%d/%m/%Y %H:%M %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual)

print(data_hora_atual.strftime(mascara_ptbr))

print(datetime.strptime(data_hora_str, mascara_en))