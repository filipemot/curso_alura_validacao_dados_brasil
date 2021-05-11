from datas_br import DatasBr
from datetime import datetime, timedelta
cadastro = DatasBr()
print(cadastro.dia_semana())
print(cadastro.format_data())

hoje = DatasBr()
print(hoje.tempo_cadastro())

