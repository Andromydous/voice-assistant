from command_fn import *
import datetime
import wikipedia
import pywhatkit
import pyjokes

wake = ""
first_time: bool = True


# *****Check for first time use and setup*******
def check_first_time():
    path = "va_name.txt"
    if os.path.exists(path):
        wake = f"{get_va_name()}"
        first_time = False
        return wake, first_time
    else:
        setup()


def get_va_name():
    path = "va_name.txt"
    f = open(path, "r")
    line = f.readline()
    va_name = f"{line.strip()}"
    f.close()
    return va_name


def set_va_name(name):
    path = "va_name.txt"
    with open(path, "a") as f:
        f.write(name)
        f.close()


def set_user_name(name):
    path = "user_name.txt"
    with open(path, "a") as f:
        f.write(name)
        f.close()


def get_user_name():
    path = "user_name.txt"
    f = open(path, "r")
    line = f.readline()
    user_name = f"{line.strip()}"
    f.close()
    return user_name


def setup():
    speech("Hello there. Since this is our first time, I need to set things up.")
    speech("In order for you to give me commands, I need a name. What would you like to call me?")
    assistant_name = get_audio().lower()
    set_va_name(assistant_name)
    speech(f"Okay, you can call me {assistant_name}. But what do I call you?")
    user_name = get_audio().lower()
    set_user_name(user_name)
    speech(f"Nice to meet you {get_user_name()}")


# **********Functions that are tied to user commands*********
def play():
    speech("What song do you want to play?")
    song = get_audio().lower()
    speech("Now playing " + song)
    pywhatkit.playonyt(song)


def jokes():
    speech("Here's a good one.")
    speech(pyjokes.get_joke())


def google_search():
    speech("What do you want me to search for?")
    search = get_audio().lower()
    speech("This is what I found on google.")
    pywhatkit.search(search)


def what_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speech("It is " + time)


def wiki_search():
    speech("What do you want me to search for?")
    new_search = get_audio().lower()
    speech("This is what I found on Wikipedia.")
    info = wikipedia.summary(new_search, 1)
    speech(info)


def my_weather():
    speech("Which city?")
    city = get_audio().lower()
    speech("For what country?")
    country = get_audio().lower()
    weather = get_weather(city, country)
    speech(weather)


def my_note():
    today = datetime.date.today()
    date2 = today.strftime("%B %d, %Y")
    speech("What do you want me to write?")
    make_mental_note(f"{date2}: {get_audio()}")
    speech("Okay. I've written it down for you.")


def open_note():
    speech("Let me look.")
    open_mental_note()


def open_program():
    speech("Which app do you want me to open?")
    program = get_audio().lower()
    app1(program)


def read_book():
    speech("Which book do you want me to read?")
    book = get_audio().lower()
    reader(book)

