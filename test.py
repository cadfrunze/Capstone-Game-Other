import datetime

timp = datetime.datetime.now()

with open('./work_log.txt', 'a') as fila:
    fila.write(f'\n{timp}')
