import pyttsx3
import speech_recognition as sr
import os
from datetime import datetime
import requests

recon = sr.Recognizer()
comando = ""


def sexta_feira_escuta():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("fale:(vindo da func)")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt').lower()
            print("Texto reconhecido: " + frase)

        except sr.UnknownValueError:
            print("Não entendi")
        return frase


def buscar_clima(cidade):
    API_KEY = "11c95aecdde84bed43cb10a7c167a494"
    city = cidade

    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"
    requisicao = requests.get(link)
    dados = requisicao.json()
    descricao = dados['weather'][0]['description']
    temp = round(dados['main']['temp'] - 273.00, 1)

    frase = "Hoje está {} na cidade {} e está fazendo {} graus".format(descricao, city, temp)

    return frase


sextaFeira = pyttsx3.init()
sextaFeira.setProperty('voice', b'brasil')
sextaFeira.setProperty('rate', 250)
sextaFeira.setProperty('volume', 1)
while True:
    resultado = sexta_feira_escuta()

    if resultado == "ok sexta feira" or resultado == "ok sexta-feira":
        sextaFeira.say("Salve mestre, o que deseja? ")
        sextaFeira.runAndWait()

        while True:
            resp = sexta_feira_escuta()
            print("depois do while true: ", resp)

            # cadastro de evento
            if resp == "cadastrar evento na agenda":
                with open("agenda.txt", 'a', encoding="utf-8") as f:
                    sextaFeira.say("Ok, qual evento devo cadastrar? ")
                    sextaFeira.runAndWait()

                    resp = sexta_feira_escuta()

                    f.write(resp)
                    f.write("\n")

                    sextaFeira.say("Evento cadastrado com sucesso! O senhor deseja mais alguma coisa?")
                    sextaFeira.runAndWait()

                    resp = sexta_feira_escuta()

                    if resp == "ler agenda" or resp == "leia agenda":
                        with open("./agenda.txt", 'r', encoding="utf-8") as agendaCadastrada:
                            fala = ",".join(agendaCadastrada.readlines())
                            print(fala)
                            sextaFeira.say(fala)
                            sextaFeira.runAndWait()
                            print("passou da leitura")

                    elif resp == "não" or resp == "nao":
                        print(resp)
                        sextaFeira.say("Ok mestre tenha um bom dia!")
                        sextaFeira.runAndWait()

                    else:
                        sextaFeira.say("O comando cadastrar evento encerrou")
                        sextaFeira.runAndWait()

            #Ler agenda (if opcional)
            if resp == "ler agenda" or resp == "leia agenda":
                with open("./agenda.txt", 'r', encoding="utf-8") as agendaCadastrada:
                    fala = ",".join(agendaCadastrada.readlines())
                    print(fala)
                    sextaFeira.say(fala)
                    sextaFeira.runAndWait()

            # toque uma musica
            if resp == "toque uma musica" or resp == "toque uma música":
                sextaFeira.say("Ok mestre, abrindo mídia")
                sextaFeira.runAndWait()
                os.system(r"D:\akon-sryBlameItOnMe.mp3")
                break

            # Perguntando a data atual
            if resp == "que dia é hoje?" or resp == "que dia é hoje":
                meses = {1: "Janeiro", 2: "fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho",
                         8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

                dia = datetime.today().day

                if datetime.today().month in meses.keys():
                    mes = meses.get(datetime.today().month)

                ano = datetime.today().year

                texto = "hoje é dia " + str(dia) + " do mês de " + str(mes) + " do ano " + str(ano)

                sextaFeira.say(texto)
                sextaFeira.runAndWait()

            # perguntando que horas sao
            if resp == "que horas são":
                agora = datetime.now()
                hora = agora.hour
                minuto = agora.minute

                texto = "Agora são " + str(hora) + " horas e " + str(minuto) + " minutos"

                sextaFeira.say(texto)
                sextaFeira.runAndWait()

            # abrir calculadora
            if resp == "abra a calculadora" or resp == "abra calculadora":
                sextaFeira.say("A calculadora está aberta, quais números deseja calcular?")
                sextaFeira.runAndWait()
                frase = sexta_feira_escuta()
                calcular = frase.split()
                if calcular[1] == 'x':
                    result = int(calcular[0]) * int(calcular[2])
                    sextaFeira.runAndWait()
                elif calcular[1] == '+':
                    result = int(calcular[0]) + int(calcular[2])
                    sextaFeira.runAndWait()
                elif calcular[1] == '-':
                    result = int(calcular[0]) - int(calcular[2])
                    sextaFeira.runAndWait()
                else:
                    result = int(calcular[0]) / int(calcular[2])
                    sextaFeira.runAndWait()

            # consultar o clima
            if resp == "qual a previsão de hoje":
                sextaFeira.say("Olá mestre, de qual cidade o senhor deseja saber o clima?")
                sextaFeira.runAndWait()

                resp = sexta_feira_escuta()

                clima = buscar_clima(resp)
                sextaFeira.say(clima)
                sextaFeira.runAndWait()
    else:
        print("Não entendi o que voce disse")
