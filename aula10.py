from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/ %m/ %y %H: %M: %S'))
    print(data_atual.strftime('%c'))
    print(data_atual.year)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2021, 11, 7, 10, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H: %M: %S')
    print(data_convertida)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A/ %B/ %Y')
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H: %M: %S')
    print(horario_str)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()
