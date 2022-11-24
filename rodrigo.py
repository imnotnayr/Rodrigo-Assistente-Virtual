## Importando as biblioteca
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys

# Criando uma instância para reconhecer a fala
listener = sr.Recognizer()

# Criando instância que será usada como referência para a fala da assistente
engine = pyttsx3.init()

# Definindo a Língua Portuguesa como idioma das pesquisas na Wikipedia
wikipedia.set_lang("pt")

# Criando uma função que faça a assistente responder o usuário com voz
def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


# Criando uma função que consiga reconhecer a fala e traduzi-la em comandos
def user_commands():
        with sr.Microphone() as source:
            print('Ouvindo...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()
            if 'rodrigo' in command:
                command = command.replace('rodrigo', ' ')
                print(command)
        
        return command


# Criando função que informa comandos para serem executados pela assistente
def run_alexa():
    command = user_commands()
    if 'toque' in command:
        song = command.replace('toque', ' ')
        print('Rodrigo: tocando ' + song + ' no Youtube')
        engine_talk('tocando' +song + ' no Youtube')
        pywhatkit.playonyt(song)
    elif 'que horas são' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Rodrigo: Agora são ' + time)
        engine_talk('Agora são' +time)
    elif 'pesquise' in command:
        search = command.replace('pesquise', ' ')
        info = wikipedia.summary(search, 2)
        print(info)
        engine_talk(info)
    elif 'qual é o seu nome' in command:
        print('Rodrigo: Pode me chamar de Rodrigo.')
        engine_talk('Pode me chamar de Rodrigo.')
    elif 'quem te criou' in command:
        print('Rodrigo: Eu fui criado pela BBT.')
        engine_talk('Eu fui criado pela BBT')


    elif 'fechar' in command:
        sys.exit()
    else:
        engine_talk("Eu não entendi. Pode repetir?")


while True:
     run_alexa()

