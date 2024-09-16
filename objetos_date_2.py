import datetime

d = datetime.datetime(2024, 9, 16, 10, 46)

print(d)

d = d + datetime.timedelta(weeks=1) #timedelta é o responsável pelas operações com data

print(d)

from datetime import date,datetime,time, timedelta

tipo_carro = 'M'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno) #podem ser utilizadas muito mais coisas do que minutos só, dias, horas, semanas, meses e etc
    print(f'O carro chegou às : {data_atual} e ficará pronto às {data_estimada}.')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou às : {data_atual} e ficará pronto às {data_estimada}.')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou às : {data_atual} e ficará pronto às {data_estimada}.')

print(date.today() - timedelta(days=1)) #operação com o data

resultado = datetime(2024, 9, 26, 11, 16) - timedelta(hours=1) #a operação com hora é feita diferente
print(resultado.time())

print(datetime.now().date())