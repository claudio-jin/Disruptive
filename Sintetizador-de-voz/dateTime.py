import pyttsx3
from datetime import datetime


meses = {1: "Janeiro", 2: "fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
         9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

agora = datetime.now()
hora = agora.hour
minuto = agora.minute
dia = datetime.today().day


print(datetime.today().month)
if datetime.today().month in meses.keys():
    mes = meses.get(datetime.today().month)
    print(mes)

ano = datetime.today().year

texto = "Agora são " + str(hora) + " horas e " + str(minuto) + " minutos"
texto += " do dia " + str(dia) + " do mês de " + str(mes) + " do ano " + str(ano)
#
# msg = "It's " + str(hora) + " Hours and " + str(minuto) + " minutes" + meses[mes] + " mes"

en = pyttsx3.init()

en.setProperty('rate', 250)
en.setProperty('volume', 1.0)
en.setProperty('voice', b'brasil')
en.say(texto)
en.runAndWait()
