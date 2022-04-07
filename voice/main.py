import os
import random
import speech_recognition


sr = speech_recognition.Recognizer()
sr.pause_threshold =0.5# тайминг по которому разделяются слова

commands_dict = {
    'commands':
        {
            'greeting': ['привет', 'приветствую'],
            'create_task':['добавить задачу', 'создать задачу', 'заметка'],
            'play_music':['включить музыку', 'дискотека']
        }
}

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(mic, duration=0.5)  # уровень шума, откалибровка микрофона
            audio = sr.listen(source=mic)  # запуск процесса прослушивания
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Пожалуста повторите'


def greeting():
    return 'Привет привет'


def create_task():
    print("Что добавим в список дел")

    query = listen_command()

    with open('file.txt', 'a') as file:
        file.write(f'{query} \n')

    return f'Задача {query} добавленна в file'


def play_music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')

    return f'Music work {random_file.split(("/")[-1])}'



def main():
    query = listen_command()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(k)

if __name__ == '__main__':
    main()
