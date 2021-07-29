from datetime import datetime
from buscador_fechas import *

try:
    nombre_dia=datetime(int(ano),int(mes),int(dia))
    print('Ese dia era/sera '+nombre_dia.strftime('%A'))
except ValueError:
    print("Esa fecha no es valida.")

