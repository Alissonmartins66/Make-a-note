import datetime
import os
import time
import speech_recognition as sr
from gtts import gTTS
import subprocess
import pygame
import tempfile


def speak(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tf:
        filename = tf.name
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()
    os.remove(filename)


def get_audio(silence_threshold=2):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception: ' + str(e))

        start_time = time.time()
        while time.time() - start_time < silence_threshold:
            audio = r.listen(source)
            try:
                new_said = r.recognize_google(audio)
                print(new_said)
                if new_said:
                    said += ' ' + new_said
                    start_time = time.time()
            except Exception as e:
                print('Exception: ' + str(e))

    return said


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


text = get_audio()


NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]
for phrase in NOTE_STRS:
    if phrase in text:
        speak("What would you like me to write down? ")
        write_down = get_audio()
        note(write_down)
        speak("I've made a note of that.")
