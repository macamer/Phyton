'''
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
'''
from datetime import datetime

#fecha actual
now = datetime.now() 
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
print(formatted_date)

#fecha de nacimiento
birth = datetime(1992, 10, 28, 8, 30, 00)
formatted_date = birth.strftime("%d/%m/%Y %H:%M:%S")
print(formatted_date)

#años transcurridos 
print(now.year - birth.year)


'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
'''
#fecha de nacimiento
birth = datetime(1992, 10, 28, 8, 30, 00)

print(f"{birth.day}/{birth.month}/{birth.year}")
print(birth.strftime("%H:%M:%S"))
