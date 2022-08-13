from playsound import playsound
import requests
import json
import os
import PyPDF2 as pdf
from os.path import exists
import pyaudio
from gtts import gTTS
import speech_recognition as sr


# **************** Convert pdf to text and tts to mp3 ***************
def pdf_convert(my_book):
    try:
        full_book = ""
        book = open(f"{my_book}.pdf", "rb")
        pdf_reader = pdf.PdfFileReader(book)
        # the starting page needs to be your selected page minus 1.
        # the ending page needs to be your selected page minus 1.
        # for pages in range(6, pdf_reader.numPages-1):
        # is range of page 7 to last page
        for pages in range(6, 8):
            page = pdf_reader.getPage(pages)
            text = page.extractText()
            page_num = str(pages + 1)
            full_book += f"{my_book} Page {page_num} {text}"
        book.close()
        return full_book
    except FileNotFoundError as e:
        print(e)
        speech("I couldn't find that book.")


# With Linux pyttsx3 sounds like a robot. 
# On the other hand, google doesn't like to translate a lot of text. 
# So gTTS can only handle a few amount of pages from pdf.
def reader(my_book):
    path = f"{my_book}.mp3"
    if os.path.exists(path):
        speech("I found it. Let me begin.")
        os.system(f"vlc {path}")
    else:
        try:
            full_book = pdf_convert(my_book)
            reading = gTTS(text=full_book, lang="en", slow=False)
            speech("Please wait while I convert the pdf to an mp3.")
            reading.save(f"{my_book}.mp3")
            speech("I finished the conversion. Let me begin")
            os.system(f"vlc {path}")
        except Exception as e:
            print(e)
            speech("I wasn't able to convert the pdf to mp3.")


# ******** When you just want to show off ************
def app1(my_app_name):
    try:
        os.system(my_app_name)
    except Exception as e:
        print(e)
        speech("I can't find that app.")


# *********** Weather Functions ****************
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


def get_api_key():
    with open("api_key.txt", "r") as f:
        return f.readline().strip()


def get_weather(city, country):
    try:
        api_key = get_api_key()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        temp_kelvin, humidity = data['main']['temp'], data["main"]["humidity"]
        description = data["weather"][0]["description"]
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        weather = f"It's {temp_fahrenheit:.2f}\u00b0 and {description}. Humidity is at {humidity}%."
        return weather
    except Exception as e:
        print(e)
        speech("I'm not able to retrieve that at this time.")


# ******** Making mental note and opening mental note
def make_mental_note(text):
    file = "notes.txt"
    with open(file, "a") as f:
        f.write(text + "\n")
        f.close()


def open_mental_note():
    file = "notes.txt"
    try:
        f = open(file, "r")
        lines = f.readlines()
        speech("Here's your notes so far:")
        for line in lines:
            speech(f"{line.strip()}")
        f.close()
    except IOError as e:
        print(e)
        speech("There's no notes for that day.")


# *********Speech to Text and Voice Recognition Engines*************
def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    playsound("output.mp3", )


def get_audio():
    command = "".lower()
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.energy_threshold = 2000
        listener.adjust_for_ambient_noise(source, 1.2)
        voice = listener.listen(source)
        print("Listening......")
    try:
        command = listener.recognize_google(voice)
        print(command)
    except Exception as e:
        print(e)
        speech("Hmm. Something went wrong.")
    return command.lower()
