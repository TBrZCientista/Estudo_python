import pytz

from datetime import datetime

d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

print(d)