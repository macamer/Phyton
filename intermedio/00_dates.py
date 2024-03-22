## Dates ##

from datetime import datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second) 


now = datetime.now() #inicializar un objeto datetime como now. Es una función propia del datetime

print_date(now)

timestamp = now.timestamp() #timestamp es una representación única de representar un tiempo
print(timestamp)

year_2025 = datetime(2025, 1, 1) #lo minimo que se necesita para definir un dia. Se pueden añadir hora, min...
print_date(year_2025)

# time
from datetime import time
current_time = time(21,6,0) #si no se define la hora se queda vacío
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


#date
from datetime import date
#current_date = date.today()
current_date = date(2022,10,6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

#hacer calculos con fechas
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date)

diff = year_2025 - now #tienen que ser objetos del mismo tipo
print(diff)
diff = year_2025.date() - current_date
print(diff)

#timedelta --> para calcular espacio de tiempo
from datetime import timedelta
init_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta+init_timedelta)
