import re

fecha=input('Favor introducir una fecha en formato DD/MM/YYYY: ')


regex_fechas=re.compile(r'^([0-3][0-9])/([0-1][1-9])/([1-2][0-9]{3})$')

v=regex_fechas.search(fecha)

print(v.groups())

dia,mes,ano=v.groups()

